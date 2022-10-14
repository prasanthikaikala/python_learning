import requests

add_supplier_url = "http://192.168.1.86:5080/add_supplier?name=Ramu"
supplier_data = {
    "company_name": "Amazon",
    "phone_no": "36478463786",
    "city": "Columbus",
    "add_line1": "8100 Edge Dr",
    "add_line2": "Unit 500",
}
add_supplier_response = requests.post(add_supplier_url, data=supplier_data)

print(add_supplier_response.text)