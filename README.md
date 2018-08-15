# Check Point API Scripts 

by: **Ryan Rasmuss**

using: [requests](https://github.com/requests) by **Kenneth Reitz** and [Check Point API](https://github.com/checkpointsw)

### Overview

- Requires ``python3``
- ``cp_api.py`` is the main script
- ``mgmt_api.sh`` is just a wrapper
- remember that any changes need to be published via ``./mgmt_api.sh publish``
- Remember to enable API on the Management Server via Smart Console
- Run ``api restart`` on Gaia

### Notes

- Use ``python3 cp_api.py`` or ``./mgmt_api.sh``
- Need to login before making api calls: ``./mgmt_api.sh login [ip_address] [port#/default] [hostname] [pw]``
- Example calls are in ``examples/examples_calls.txt``


### Special Cases

If you have to build a request with lists of objects such as adding multiple hosts to a new group:

```shell
POST {{server}}/add-group
Content-Type: application/json
X-chkp-sid: {{session}}

{
  "name" : "New Group 4",
  "members" : [ "New Host 1", "My Test Host 3" ]
}
```

The script will expect the members objects to be contained in quotes(``"``) with commas as delimiters(``,``). 

For example: ``python3 cp_api.py add-group name "New Group 4" members "New Host 1, My Test Host 3"``

Make sure you build the host objects before running this command.


If you have to build a request with the following structure:

```shell
POST {{server}}/set-group
Content-Type: application/json
Ses: 
X-chkp-sid: {{session}}

{
  "name" : "New Group 1",
  "members" : {
    "add" : "New Host 1", "My Test Host 3"
  },
}
```

The script will expect a colon(``:``) to denote the nested key-value pairs.

For example: ``python3 cp_api.py set-group name "New Group 1" members "add:My Test Host 3,New Host 1"``


### ToDo

- [x] Delete session contents after logouts
- [x] Parse nested json
- [x] Publish
- [x] Start adding other commands
- [x] Add new gateway w/ sic
- [x] After posts, send message to remind to publish changes!
- [x] Throw in a main()
