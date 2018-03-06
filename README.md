# Check Point API Scripts 

by: **Ryan Rasmuss**
using: **requests by Kenneth Reitz**, **Check Point API** 

### Overview

- Requires ``python3``
- ``cp_api.py`` is the main dev script
- ``mgmt_api.sh`` is just a wrapper
- remember that any changes need to be published via ``./mgmt_api.sh publish``

### Notes

- Can make calls in two way: ``python3 cp_api.py`` or ``./mgmt_api.sh``
- Need to call setup before making api calls: ``./mgmt_api.sh setup [ip_address] [port#/default] [hostname] [pw]``
- Example calls are in ``examples/examples_calls.txt``

### ToDo

- [ ] Need to parse arguments better, need to be able to navigate commands like VBoxManage
- [x] Publish
- [x] Start adding other commands
- [x] Add new gateway w/ sic
- [x] After posts, send message to remind to publish changes!
- [ ] Throw in a main()