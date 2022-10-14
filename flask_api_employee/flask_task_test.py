import requests
import json
url="http://127.0.0.1:5000/add_phonenumber?name=\"RAJU\"&phone_no=\"5555555555\"&city=\"HYD\""

response = requests.get(url)
print(response.status_code)
#print(response.text)
ret_dic = json.loads(response.text)
print(ret_dic)
