# Demo to add servers to existing group

server_two=('prod-server-2' '2.2.2.2')
server_three=('prod-server-3' '3.3.3.3')
server_four=('prod-server-4' '4.4.4.4')

servers=(server_two[@] server_three[@] server_four[@])
names=''

COUNT=${#servers[@]}

for ((i=0; i <$COUNT; i++))
do
    name=${!servers[i]:0:1}
    ip=${!servers[i]:1:1}
    #echo $name
    #echo $ip
    ./mgmt_api.sh add-host name $name ip-address $ip color blue
    names+=$name
    if [[ $COUNT-1 -ne $i ]]
    then
        names+=","
    fi
done

#echo $names

./mgmt_api.sh set-group name servers members add:$names
