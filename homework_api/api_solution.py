import requests

name_api_url = "http://192.168.1.86:5000/name_api?name=Satya&phone_no=9089067890&city=BLR"
name_response = requests.get(name_api_url)
print("Response code for name_api = ", name_response.status_code)
print("Response for name_api = ", name_response.text)
