import requests

employee_api_url = "http://192.168.1.86:5000/employee_api?employee_name=Manu&designation=engineer&location=hyd"
employee_response = requests.get(employee_api_url)
print("Response code for employee_api = ",employee_response .status_code)
print("Response for employee_api = ", employee_response.text)

search_api_url = "http://192.168.1.86:5000/search_employee?employee_name=sunny"
search_response = requests.get(search_api_url)
print("Response code for search_api = ", search_response.status_code)
print("Response for search_api = ",search_response.text)

delete_api_url = "http://192.168.1.86:5000/delete_employee?employee_name=ganesh"
delete_response = requests.get(delete_api_url)
print("Response code for delete_api = ", delete_response.status_code)
print("Response for delete_api = ", delete_response.text)

get_all_api_url = "http://192.168.1.86:5000/get_all_employee_in_location?location=hyd"
get_response = requests.get(get_all_api_url)
print("Response code for get_api = ", get_response.status_code)
print("Response for get_api = ", get_response.text)