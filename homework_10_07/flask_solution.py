import requests

add_api_url = "http://192.168.1.86:5000/add_api?param1=300&param2=500"
output_file = "C:\\Users\\kaika\\Desktop\\prasanthi\\homework_10_07\\output.txt"

add_response = requests.get(add_api_url)
print("Response code for add_api = ", add_response.status_code)
print("Response for add_api = ", add_response.text)
jsonfile = open(output_file, 'w')
jsonfile.write(add_response.text)
jsonfile.write("\n\n")

multiply_api_url = "http://192.168.1.86:5000/multiply_api?param3=300&param4=100"

multiply_response = requests.get(multiply_api_url)
print("Response code for multiply_api = ", multiply_response.status_code)
print("Response for multiply_api = ", multiply_response.text)

jsonfile.write(multiply_response.text)
jsonfile.write("\n\n")
jsonfile.close()

