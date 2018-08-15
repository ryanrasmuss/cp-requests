#!/bin/bash

declare -a hosts=("prod-server-1" "prod-server-2" "prod-server-3" "prod-server-4")

./mgmt_api.sh delete-group name servers

for host in "${hosts[@]}"
do
    ./mgmt_api.sh delete-host name $host
done

./mgmt_api.sh publish
