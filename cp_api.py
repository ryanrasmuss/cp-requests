import requests, json
from getpass import getpass as gp
from helper import helper
from api_headers import api_call
from api_headers import login
from os import stat
from sys import argv

session_file = 'session.txt'
out_file = 'output.txt'
colon = ':'
delim = '\n'
comma = ','

def list_parser(parse_me):

    parsed = parse_me.split(colon)
    rturner = {}

    token = ''

    for element in parsed:
        if parsed[0] == element:
            token = element
        elif element == parsed[-1]:
            rturner[token] = element.split(comma)
        else:
            objs = element.split(comma)
            rturner[token] = objs[:-1]
            token = objs[-1]

    return rturner


def get_payload(requirements):

    return_me = {}
    nested = 0

    if len(requirements) % 2 != 0:
        print("Error: expecting even number of arguments aside from command")
        return return_me

    ''' iterate over every other two '''
    for i in range(0, len(requirements), 2):
        if colon in requirements[i+1]:
            return_me[requirements[i]] = list_parser(requirements[i + 1])
        elif comma in requirements[i+1]:
            return_me[requirements[i]] = requirements[i + 1].split(comma)
        else:
            return_me[requirements[i]] = requirements[i+1]

    print(return_me)
    return return_me

''' Print Help '''

def help():

    print("\nUsage:  mgmt_api.sh login [mgmt_ip_addr] [port#] [username]")
    print("\tmgmt_api.sh [command] {parameters}")
    print("\tmgmt_api.sh publish")
    print("\tmgmt_api.sh logout\n")


''' Setup Function - For initial connection to Management Server '''

def setup(argv):

    if len(argv) == 5 or len(argv) == 6:

        address = argv[2]

        if argv[3] == 'default':
            port = '443'
        else:
            port = argv[3]

        username = argv[4]  
        if len(argv) == 6:
            password = argv[5]
        else:
            password = gp("Password: ")

        #f = open(session_file, "w+")

        sid = login(username, password, address, port)
        if None == sid:
            return None
        
        f = open(session_file, "w+")
        
        filesize = stat(session_file).st_size

        if filesize != 0:
            print("There seems to be another session already esatablished.")
            with open(session_file, "r") as f:
                print (f.read())
            print("Please terminate this session before logging in. Try logout.")
            return None

        f.write(address + delim)
        f.write(port + delim)
        f.write(sid)
        f.close()

        print("Done setting up")
        print ("Created session file: " + session_file)
    else:
        print("\nParameters are weird. Try again.")
        help()


''' Retrieve Session Information '''
def get_session_data(session_file):

    with open(session_file) as f:
        data = f.read()

    data = data.split(delim)
    f.close()
    
    return data

''' Main Function '''

def main():

    specials = [ 'publish', 'discard', 'logout' ]
    immutable = 'show'

    if len(argv) == 1:
        help()
    elif argv[1] == 'login':
        setup(argv)
    else:
        try:
            session_data = get_session_data(session_file)

            address, port, sid = session_data[0], session_data[1], session_data[2]

            command = argv[1]

            if 'logout' == argv[1]:
                session_fd = open(session_file, 'w')
                session_fd.truncate()

            ''' Actual Parsing '''
            payload = get_payload(argv[2:])

            response = api_call(address, port, command, payload, sid)
            data = response.json()
            pretty_print = json.dumps(data, indent=4, sort_keys=False)

            with open(out_file, "w") as f:
                f.write(pretty_print)
            f.close()

            print("Wrote response to %s" % out_file)

            status = str(response.status_code)
            print ("Status code: %s" % (status))

            if (status == '200') and (argv[1] not in specials) and (immutable not in argv[1]):
                print("\n\tRemember to publish changes via: \"python3 cp_api.py publish\"\n")
            elif status == '409':
                print("\n\tProblem with locks. Make sure you are publishing and terminating sessions properly.\n")
            elif status == '404':
                print("\nI don't recognize the command: %s\n" % (argv[1]))
                helper(argv[1])
            elif status == '400':
                print("\nMissing command parameters. Refer to output.txt\n")
            elif status == '401':
                print("\nSession Expired. You need to login.\n")
                session_fd = open(session_file, 'w')
                session_fd.truncate()
            else:
                print('Response: %s (Check output.txt for more)' % (response.status_code))

        except:
            print('\nWhat? Try logging in.')
            help()


if __name__ == '__main__':
    main()
