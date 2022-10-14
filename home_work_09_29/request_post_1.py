import requests
import json
token ="50a9401d9598c69e94e906188f497fcadd1feab941fba66ca38926fd91ff8d03"

headers_1 = {\
    "Authorization": "Bearer 50a9401d9598c69e94e906188f497fcadd1feab941fba66ca38926fd91ff8d03",\
           "Accept":"application/json",\
           "Content-Type":"application/json"}
url_1="https://gorest.co.in/public/v2/users"
data_1={"name":"Python Tuple", "gender":"male",
"email":"python.tuple@15ce.com",
"status":"active"}
response=requests.post(url=url_1,data=json.dumps(data_1),headers=headers_1)
"""
response=requests.post(url=url_1,data=json.dumps(data_1),headers=headers_1,\
                       auth=("username","password")
"""
print(response.status_code)
response_result=response.text

d1= json.loads(response_result)
print(d1)



"""
curl -i -H "Accept:application/json"
-H "Content-Type:application/json"
-H "Authorization: Bearer 50a9401d9598c69e94e906188f497fcadd1feab941fba66ca38926fd91ff8d03"
-XPOST "https://gorest.co.in/public/v2/users" -d
'{"name":"Tenali Ramakrishna", "gender":"male",
"email":"tenali.ramakrishna@15ce.com",
"status":"active"}'

"""
