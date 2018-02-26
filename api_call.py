import requests, json

''' verify=False in requests calls; L2 install cert for vms '''

ap_addr = '192.168.26.100'
port ='443'
username = 'admin'
pw = 'vpn123'


def api_call(ip_addr, port, command, json_payload, sid):

    url = 'https://' + ip_addr + ':' + port + '/web_api/' + command
    print ("Making request to: " + url)
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)
    print (r)
    return r.json()

def login(user, password, addr, port):
    payload = {'user': user, 'password': password}
    response = api_call(addr, port, 'login', payload, '')
    return response["sid"]

sid = login(username, pw, ap_addr, port)
print ("SID: " + sid)

new_host_data = {'name': 'API-Ryan', 'ip-address': '192.168.26.10'}
new_host_result = api_call(ap_addr, port, "add-host", new_host_data, sid)
print(json.dumps(new_host_result))

publish_result = api_call(ap_addr, port, "publish", {}, sid)
print("publish result: " + json.dumps(publish_result))

logout_result = api_call(ap_addr, port, "logout", {}, sid)
print("logout result: " + json.dumps(logout_result))