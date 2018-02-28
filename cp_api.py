import requests, json
from api_headers import api_call
from api_headers import login
from sys import argv

session_file = 'session.txt'
out_file = 'cp_output.txt'
delim = '\n'

''' how do I want this script to work .. '''

''' python3 cpi_api.py setup [address] [port] [username] [password] '''
''' find a better way to use username and password '''
''' store this info in a file cpi_api.txt '''

''' python3 cpi_api.py payload 

  mgmt_cli add host [name] [ip-address] [xxx.xxx.xxx.xxx]
  api_call needs (command, payload)
    "add-host" {'name': [name], 'ip-address': '[ip-address]' }

  mgmt_cli network name [name] subnet [subnet] mask-length [24]
        ASSUMING API CALL WOULD LOOK LIKE
    "add-network" {'name': [name], 'subnet': '[subnetid]', 'mask-length': '[cidr]'}'''

def help_args(command):
    print ("Hi, purpose is to give responses to help use this script")
    print ("Think of VBoxManage script")

    if command is "setup":
        print ("Print setup help")
    elif command is "add-access-rule":
        print ("add-access-rule help")
    else:
        print ("Supported Commands (should be same as first script run")
        

def get_payload(requirements):

    return_me = {}

    if len(requirements) % 2 != 0:
        print("Error: expecting even number of arguments aside from command")
        return return_me

    ''' iterate over every other two '''
    for i in range(0, len(requirements), 2):
        return_me[requirements[i]] = requirements[i+1]

    print(return_me)
    return return_me


''' XXX: DISCLAIMER! This is bad implementation, do not use in production '''

''' XXX: Make setup functions, make setup, login, add-host, add-network, logout, etc '''

if len(argv) == 1:
    print("\nUsage:  python3 cp_api.py setup [mgmt_ip_addr] [port#] [username] [password]")
    print("\tpython3 cp_api.py [command] {parameters}")
    print("\tpython3 cp_api.py logout")
    print("\tpython3 cp_api.py publish\n")

elif argv[1] == 'setup' and len(argv) == 6:

    address = argv[2]

    if argv[3] == 'default':
        port = '443'
    else:
        port = argv[3]

    username = argv[4]  
    password = argv[5]

    f = open(session_file, "w+")
    sid = login(username, password, address, port)
    f.write(address + delim)
    f.write(port + delim)
    f.write(sid)
    f.close()

    print("Done setting up")
    print ("Created session file: " + session_file)

    exit
else:
    with open(session_file) as f:
        data = f.read()
    print("data: " + data)
    data = data.split('\n')
    f.close()

    address = data[0]
    port = data[1]
    sid = data[2]

    print("Retrieved: " + address + " " + port + " " + sid)

    print("The Command is: " + argv[1])

    print("Crap I need to format: ")
    for req in argv[2:]:
        print(req)

    print("Parsing requirements")
    payload = get_payload(argv[2:])

    response = api_call(address, port, argv[1], payload, sid)
    data = response.json()
    pretty_print = json.dumps(data, indent=4, sort_keys=False)

    print ("Status code returned: " + str(response.status_code))

    with open(out_file, "w") as f:
        f.write(pretty_print)
    f.close()

    print("Wrote response to %s" % out_file)

    if str(response.status_code) == '200' and len(argv) > 3:
        print("\n\tRemember to publish changes via: \"python3 cp_api.py publish\"\n")