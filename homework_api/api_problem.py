import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/name_api', methods=['GET'])
def name_api():
    name = request.args.get("name")
    phone_no = request.args.get("phone_no")
    city = request.args.get("city")
    r1 = {}
    contacts_list = []
    phone_book_path = "\\Users\\kaika\\Desktop\\prasanthi\\homework_api\\phone_book.json"
    with open(phone_book_path, "r") as phone_book:
        contacts_list.extend(json.load(phone_book))
        for contact in contacts_list:
            r1[contact['name']] = {"name": contact["name"], "phone_no": contact["phone_no"], "city": contact["city"]}
            print(contact)

    if name in r1.keys():
        print("% already exist" % name)
        return "%s is already exist" % name
    else:
        new_contact = {"name": name, "phone_no": phone_no, "city": city}
        contacts_list.append(new_contact)
        with open(phone_book_path, "w") as phone_book1:
            json.dump(contacts_list, phone_book1, indent=4)
    return "Added new contact %s phone book" % name


if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.1.86", port=5000)
