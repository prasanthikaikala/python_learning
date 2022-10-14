from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add_api', methods=['GET'])
def add_api():
    num1 = request.args.get("param1")
    num2 = request.args.get("param2")
    r1 = {}
    total = int(num1) + int(num2)
    print("Addition of %s + %s  = %s" % (num1, num2, total))
    r1["Addition"] = total
    return jsonify(r1)


@app.route('/multiply_api', methods=['GET'])
def multiply_api():
    numb1 = request.args.get("param3")
    numb2 = request.args.get("param4")
    r2 = {}
    total = int(numb1) * int(numb2)
    print("Multiplication of %s x %s  = %s" % (numb1, numb2, total))
    r2["Multiplication"] = total
    return jsonify(r2)


if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.1.86", port=5000)
