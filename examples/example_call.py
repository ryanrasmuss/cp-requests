import requests, json

ap_addr = "192.168.26.100"
port = '443'
username = 'admin'
pw = 'vpn123'

''' This garbage is broken, can't translate int (443) to string
    ap_addr is not defined in api_call, assuming they meant ip_addr 
    not certificate, so requests will throw ssl certificate error and stop '''

def api_call(ip_addr, port, command, json_payload, sid):
    url = 'https://' + ap_addr + ':' + port + '/web_api/' + command
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers)
    return r.json()


def login(user,password):
    payload = {'user':user, 'password' : password}
    response = api_call('192.168.65.2', 443, 'login',payload, '')
    return response["sid"]

sid = login(username,pw)
print("session id: " + sid)

new_host_data = {'name':'new host name', 'ip-address':'192.168.1.1'}
new_host_result = api_call('192.168.65.2', 443,'add-host', new_host_data ,sid)
print(json.dumps(new_host_result))

publish_result = api_call('192.168.65.2', 443,"publish", {},sid)
print("publish result: " + json.dumps(publish_result))

logout_result = api_call('192.168.65.2', 443,"logout", {},sid)
print("logout result: " + json.dumps(logout_result))	