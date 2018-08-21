# Check Point API & Requests

by: **Ryan Rasmuss**

using: [requests](https://github.com/requests) by **Kenneth Reitz** and [Check Point API](https://github.com/checkpointsw)

A simple tool to make API calls to a Check Point R80 Management Server.

## Overview

- Requires ``python3``
- ``cp_api.py`` is the main script
- ``mgmt_api.sh`` is just a wrapper 
- You need to make a login request before making api calls: ``./mgmt_api.sh login [ip_address] [port#/default] [hostname]``
- Any changes you make need to be published (saved) via ``./mgmt_api.sh publish``
- Remember to enable API on the Management Server via Smart Console
- Run ``api restart`` on Gaia if you have diffulties connecting to the Management Server
- Example calls are in ``examples/examples_calls.txt``

Refer to the [Check Point API](https://sc1.checkpoint.com/documents/latest/APIs/index.html#introduction~v1.2%20) and the [R80 Admin Guide](http://dl3.checkpoint.com/paid/29/29ba43867b6b7fc08559fadbcf2226fc/CP_R80.10_SecurityManagement_AdminGuide.pdf?HashKey=1534827596_41e9be562f6a20ffdca38a53c306430d&xtn=.pdf) page 25.

## Check Point API Workflow

1. ``login`` to create an active session
2. Do work (add/show/change/remove objects)
3. ``publish`` or ``discard``
4. ``logout`` to safely terminate your session

## Special Cases

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


If you have to build a request with an embedded key-value pair like adding new hosts to an existing group:

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


## ToDo

- [ ] Install script
- [ ] Safely handle dangling sessions
- [x] Workflow documentation
- [x] Delete session contents after logouts
- [x] Parse nested json
- [x] Publish
- [x] Start adding other commands
- [x] Add new gateway w/ sic
- [x] After posts, send message to remind to publish changes!
- [x] Throw in a main()
