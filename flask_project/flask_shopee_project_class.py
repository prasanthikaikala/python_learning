from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopee.sqlite3'
app.config['SECRET_KEY'] = "qwerty"

db = SQLAlchemy(app)


class supplier(db.Model):
    id = db.Column('supplier_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    phone_no = db.Column(db.String(13))
    city = db.Column(db.String(50))
    add_line1 = db.Column(db.String(50))
    add_line2 = db.Column(db.String(50))

    def __init__(self, name, company_name, phone_no, city, \
                 add_line1, add_line2):
        self.name = name
        self.company_name = company_name
        self.phone_no = phone_no
        self.city = city
        self.add_line1 = add_line1
        self.add_line2 = add_line2


"""
add_supplier (POST)
get_sup_id(GET)
"""


class consumer(db.Model):
    id = db.Column('consumer_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone_no = db.Column(db.String(13))
    city = db.Column(db.String(50))
    add_line1 = db.Column(db.String(50))
    add_line2 = db.Column(db.String(50))

    def __init__(self, name, phone_no, city, \
                 add_line1, add_line2):
        self.name = name
        self.phone_no = phone_no
        self.city = city
        self.add_line1 = add_line1
        self.add_line2 = add_line2


"""
add_consumer (POST)
get_con_id(GET)

"""


class product(db.Model):
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    supplier_id = db.Column(db.Integer)

    def __init__(self, name, price, supplier_id):
        self.name = name
        self.price = price
        self.supplier_id = supplier_id


@app.route('/add_product/', methods=['POST'])
def new_emp():
    if request.method == 'POST':
        if not request.args.get('name') or not request.form['price'] or not \
                request.form['supplier_id']:
            return jsonify({-1: "needed form ids in form doesnot exist"})
        else:
            try:
                n1 = request.form['name']
                d1 = request.form['price']
                s1 = request.form['supplier_id']
                p1 = product(n1, d1, s1)
                db.session.add(p1)
                db.session.commit()
                return jsonify({200: "product successfully added"})
            except Exception as Error:
                print("exception occured " + str(Error))
                return jsonify({-1: "Failure in product addition " + str(Error)})
    else:
        return jsonify({-1: "This is only POST call "})


@app.route('/get_pro_id', methods=['GET'])
def get_product_id():
    if request.method == 'GET':
        # emp_list = employee.query.filter_by(name=request.args.get('name'))
        n1 = request.args.get('name')
        pro_list = product.query.filter(product.name.contains(n1))
        e_l1 = []
        for e1 in pro_list:
            e_l1.append(e1.product_id)
        return jsonify(e_l1)


class purchase_tr(db.Model):
    id = db.Column('purchase_tr_id', db.Integer, primary_key=True)
    consumer_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer)
    cost = db.Column(db.Float)

    def __init__(self, consumer_id, product_id, supplier_id, cost):
        self.consumer_id = consumer_id
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.cost = cost


"""
add transaction(POST)
get_tr_id (GET)
"""

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host="127.0.0.1", port=5000)
