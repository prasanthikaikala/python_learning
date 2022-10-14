import json

from flask import Flask, request, jsonify

app = Flask(__name__)

employee_json_path = "\\Users\\kaika\\Desktop\\prasanthi\\flask_api_employee\\employee.json"


@app.route('/employee_api', methods=['GET'])
def add_employee():
    if request.method == 'GET':
        employee_name = request.args.get('employee_name')
        designation = request.args.get('designation')
        location = request.args.get('location')
        r1 = {}
        employee_list = []
        with open(employee_json_path, 'r') as f1:
            employee_list.extend(json.load(f1))
            for employee in employee_list:
                r1[employee['employee_name']] = {"employee_name": employee["employee_name"],
                                                 "designation": employee["designation"],
                                                 "location": employee["location"]}
                print("Employee = ", employee)

        if employee_name in r1.keys():
            r_dict = {"status": -1, "message": "Employee with name %s already exists." % employee_name}
            return jsonify(r_dict)
        else:
            new_employee = {"employee_name": employee_name, "designation": designation, "location": location}
            employee_list.append(new_employee)
            with open(employee_json_path, 'w') as f2:
                json.dump(employee_list, f2, indent=4)
                r_dict = {"status": 0, "message": "New employee %s successfully added" % employee_name}
        return jsonify(r_dict)


@app.route('/search_employee', methods=['GET'])
def search_employee():
    if request.method == 'GET':
        employee_name = request.args.get('employee_name')
        r1 = {}
        employee_list = []
        with open(employee_json_path, 'r') as f1:
            employee_list.extend(json.load(f1))
            for employee in employee_list:
                r1[employee['employee_name']] = {"employee_name": employee["employee_name"],
                                                 "designation": employee["designation"],
                                                 "location": employee["location"]}
                print("Employee = ", employee)

        if employee_name in r1.keys():
            r_dict = {"status": 0, "message": "Employee with name %s found." % employee_name,
                      "Employee": r1[employee_name]}
            return jsonify(r_dict)
        else:
            r_dict = {"status": -1, "message": "Employee %s not found" % employee_name}
        return jsonify(r_dict)


@app.route('/delete_employee', methods=['GET'])
def delete_employee():
    if request.method == 'GET':
        employee_name = request.args.get('employee_name')
        employee_list = []
        with open(employee_json_path, 'r') as f1:
            employee_list.extend(json.load(f1))
            for employee in employee_list:
                if employee_name == employee["employee_name"]:
                    employee_list.remove(employee_name)
                    r_dict = {"status": 0, "message": "Employee with name %s deleted." % employee_name,}
                    return jsonify(r_dict)
                else:
                    r_dict = {"status": -1, "message": "Employee %s is not exist" % employee_name}
                return jsonify(r_dict)



@app.route('/get_all_employee_in_location', methods=['GET'])
def get_all_employee():
    if request.method == 'GET':
        location = request.args.get('location')
        employee_list = []
        filtered_list = []
        with open(employee_json_path, 'r') as f1:
            employee_list.extend(json.load(f1))
            for employee in employee_list:
                if location == employee["location"]:
                    filtered_list.append(employee)

        return jsonify(filtered_list)


if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.1.86", port=5000)
