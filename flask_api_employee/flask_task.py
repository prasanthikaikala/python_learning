import json

from flask import Flask, request, jsonify

app = Flask(__name__)

file_name = "phone_contacts.json"


@app.route('/add_phonenumber', methods=['GET'])
def add_number():
    if request.method == 'GET':
        n1 = request.args.get('name')
        ph_no = request.args.get('phone_no')
        c1 = request.args.get('city')
        r1 = {}
        r1[n1] = {"phone_no": ph_no, "city": c1}
        ph_list = []
        with open(file_name, 'r') as f1:
            ph_list = json.load(f1)
        for i1 in ph_list:
            if list(i1.keys())[0] == n1:
                r_dict = {"status": -1, "message": "contact with this name already exists"}
                return jsonify(r_dict)
        ph_list.append(r1)
        with open(file_name, 'w') as f2:
            ph_list = json.dump(ph_list, f2)
        r_dict = {"status": 0, "message": "contact succesfully added"}
        return jsonify(r_dict)


@app.route('/search_phonenumber', methods=['GET'])
def search_number():
    if request.method == 'GET':
        n1 = request.args.get('name')
        ph_list = []
        with open(file_name, 'r') as f1:
            ph_list = json.load(f1)
        for i1 in ph_list:
            if list(i1.keys())[0] == n1:
                r_dict = {"status": 100, "message": "contact with this name exists"}
                return jsonify(r_dict)
        r_dict = {"status": 200, "message": "contact with this name not exists"}
        return jsonify(r_dict)


@app.route('/delete_phonenumber', methods=['GET'])
def delete_number():
    if request.method == 'GET':
        n1 = request.args.get('name')
        ph_list = []
        with open(file_name, 'r') as f1:
            ph_list = json.load(f1)
        for i1 in ph_list:
            if list(i1.keys())[0] == n1:
                ph_list.remove(i1)
                with open(file_name, 'w') as f2:
                    ph_list = json.dump(ph_list, f2)
                r_dict = {"status": 0, "message": "contact removed successfully"}
                return jsonify(r_dict)
        r_dict = {"status": -1, "message": "contact with this name not exists"}
        return jsonify(r_dict)


@app.route('/get_phonenumber', methods=['GET'])
def get_number():
    if request.method == 'GET':
        n1 = request.args.get('name')
        ph_list = []
        with open(file_name, 'r') as f1:
            ph_list = json.load(f1)
        for i1 in ph_list:
            if list(i1.keys())[0] == n1:
                r_dict = {"status": 0, "message": "contact exists", "phone_no": i1.phone_no}
                return jsonify(r_dict)
        r_dict = {"status": -1, "message": "contact with this name not exists"}
        return jsonify(r_dict)


@app.route('/get_all_phonenumber_in_a_city', methods=['GET'])
def get_all_numbers():
    if request.method == 'GET':
        n1 = request.args.get('city')
        ph_list = []
        with open(file_name, 'r') as f1:
            ph_list = json.load(f1)
        no_list = []
        for i1 in ph_list:
            if n1 in i1.values():  # tobe checked
                no_list.append(i1.phone_no)
                r_dict = {"status": 0, "message": "contact exists", "phone_no_list": no_list}
                return jsonify(r_dict)


@app.route('/f_api', methods=['GET'])
def first_api():
    if request.method == 'GET':
        n1 = request.args.get('name')
        r1 = {}
        r1["k1"] = "hello {}".format(n1)
        return jsonify(r1)


if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=5000)
