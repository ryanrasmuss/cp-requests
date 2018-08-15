#!/bin/bash

host=('prod-server-1' '1.1.1.1' 'red')

./mgmt_api.sh add-host name ${host[0]} ip-address ${host[1]} color ${host[2]}
./mgmt_api.sh add-group name servers members ${host[0]}
