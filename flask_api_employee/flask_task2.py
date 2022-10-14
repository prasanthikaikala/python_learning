from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY'] = "qwerty"

db = SQLAlchemy(app)

class employee(db.Model):
   id = db.Column('emp_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   department = db.Column(db.String(50))

   def __init__(self, name, department):
      self.name = name
      self.department = department

@app.route('/')
def list_all():
    emps = employee.query.all()
    e_list = []
    for e1 in emps:
        e_list.append(e1.name)
    return jsonify(e_list)

@app.route('/new_emp/', methods = ['GET','POST'])
def new_emp():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['department']:
         print("needed form ids in form doesnot exist")
      else:
         n1=request.form['name']
         d1=request.form['department']
         emp = employee(n1,d1)        
         db.session.add(emp)
         db.session.commit()
         return jsonify({1:200})
   else:
        return jsonify({2:300})

@app.route('/search', methods = ['GET'])
def search():
   if request.method == 'GET':
      #emp_list = employee.query.filter_by(name=request.args.get('name'))
      n1=request.args.get('name')
      emp_list = employee.query.filter(employee.name.contains(n1))
      e_l1=[]
      for e1 in emp_list:
          e_l1.append(e1)
      return jsonify(e_l1)         
   

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.debug=True
    app.run(host="127.0.0.1",port=5000)

"""
POST call how to access data
sqlalchemy use adding data into the db
db query
"""
