import requests
from api_headers import api_call
from api_headers import login
from sys import argv

api_persistence_file = 'cpi_api.txt'
sid_persistence_file = 'sid.txt'

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

def get_payload(requirements):

    return_me = {}

    for index in range(0, len(requirements)):
        print(requirements[index])






'''
special cases:

"publish" {}
"logout" {}
"login" will use cpi_api.txt and dump a sid.txt

'''

''' XXX: DISCLAIMER! This is bad implementation, do not use in production '''

''' XXX: Make setup functions, make setup, login, add-host, add-network, logout, etc '''

delim = '\n'

if len(argv) == 1:
    print("Usage: python3 cpi_api.py setup [mgmt_ip_addr] [port#] [username] [password]")

elif argv[1] == 'setup' and len(argv) == 6:

    address = argv[2]

    if argv[3] == 'default':
        port = '443'
    else:
        port = argv[3]

    username = argv[4]  
    password = argv[5]

    f = open('sid.txt', "w+")
    sid = login(username, password, address, port)
    f.write(sid)
    f.close()

    print("Done setting up")
    print ("Created sid.txt")

    exit
else:
    with open(sid_persistence_file) as f:
        sid = f.read()
    print("sid: " + sid)

    print("The Command is: " + argv[1])
    print("Crap I need to format: ")
    for req in argv[2:]:
        print(req)

    