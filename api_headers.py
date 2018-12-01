import requests, json

def api_call(ip_addr, port, command, json_payload, sid):

    print(json_payload)

    url = 'https://' + ip_addr + ':' + port + '/web_api/' + command
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}

    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)

    debug_data = json.dumps(json_payload)
    print(debug_data)

    return r

def login(user, password, addr, port):
    payload = {'user': user, 'password': password}
    response = api_call(addr, port, 'login', payload, '')
    code = str(response.status_code)
    if code != '200':
        print("Problem logging in")
        print(response.json())
        return None
    data = response.json()
    return data["sid"]
