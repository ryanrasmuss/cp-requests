import requests, json
from api_headers import api_call
from api_headers import login
from sys import argv

session_file = 'session.txt'
out_file = 'cp_output.txt'
delim = '\n'
comma = ','


''' XXX: parse arguments given by user '''
''' XXX: current problem list requirements
   service "ssh, ssh_version_2" '''
def get_payload(requirements):

    return_me = {}

    if len(requirements) % 2 != 0:
        print("Error: expecting even number of arguments aside from command")
        return return_me

    ''' iterate over every other two '''
    for i in range(0, len(requirements), 2):
        return_me[requirements[i]] = requirements[i+1]
        if comma in requirements[i+1]:
            return_me[requirements[i]] = requirements[i + 1].split(comma)
        else:
            return_me[requirements[i]] = requirements[i+1]


    print(return_me)
    return return_me

''' Print Help '''

def help():

    print("\nUsage:  python3 cp_api.py setup [mgmt_ip_addr] [port#] [username] [password]")
    print("\tpython3 cp_api.py [command] {parameters}")
    print("\tpython3 cp_api.py publish")
    print("\tpython3 cp_api.py logout\n")


''' Setup Function - For initial connection to Management Server '''

def setup(argv):

    address = argv[2]

    if argv[3] == 'default':
        port = '443'
    else:
        port = argv[3]

    username = argv[4]
    password = argv[5]

    print("Writing username and password: " + username + " " + password)

    f = open(session_file, "w+")
    sid = login(username, password, address, port)
    f.write(address + delim)
    f.write(port + delim)
    f.write(sid)
    f.close()

    print("Done setting up")
    print ("Created session file: " + session_file)

''' Retrieve Session Information '''

def get_session_data(session_file):

    with open(session_file) as f:
        data = f.read()

    print("data: " + data)
    data = data.split(delim)
    f.close()
    
    return data

''' Main Function '''

def main():

    if len(argv) == 1:
        help()
    elif argv[1] == 'setup' and len(argv) == 6:
        setup(argv)
    else:
        session_data = get_session_data(session_file)

        address, port, sid = session_data[0], session_data[1], session_data[2]

        print("Retrieved: " + address + " " + port + " " + sid)
        print("The command is: " + argv[1])

        print("Going to parse the following arguments..")

        for req in argv[2:]:
            print(req)

        command = argv[1]

        ''' Actual Parsing '''
        payload = get_payload(argv[2:])
        ''' Making API Call '''
        print("Making API call..")
        response = api_call(address, port, command, payload, sid)
        data = response.json()
        pretty_print = json.dumps(data, indent=4, sort_keys=False)

        print ("Status code returned: " + str(response.status_code))

        with open(out_file, "w") as f:
            f.write(pretty_print)
        f.close()

        print("Wrote response to %s" % out_file)

        if str(response.status_code) == '200' and len(argv) > 3:
            print("\n\tRemember to publish changes via: \"python3 cp_api.py publish\"\n")

if __name__ == '__main__':
    main()
