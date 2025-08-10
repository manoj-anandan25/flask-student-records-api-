from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    grade = db.Column(db.String(80), nullable = False)
    rollnumber = db.Column(db.Integer, nullable = False) 
    
    def __repr__(self):
        return f"<Student {self.name}--{self.age}--{self.grade}--{self.rollnumber}"
    
@app.route('/')
def home():
    return'Welcome to student record!'

@app.route('/students')
def get_students():
    students = Student.query.all()
    output = []
    for student in students:
        student_data = {"name":student.name,"age":student.age,"grade":student.grade,"rollnumber":student.rollnumber}
        output.append(student_data)
    return {"Students":output}

@app.route('/students/<id>')
def get_student(id):
    student = Student.query.get(id)
    return {"name":student.name,"age":student.age,"grade":student.grade,"rollnumber":student.rollnumber}

@app.route('/students/<id>', methods =['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student is None:
        return {"error":"Not Found"}
    db.session.delete(student)
    db.session.commit()
    return{"message":"yeet!@"}

@app.route('/students', methods =['POST'])
def add_student():
    student = Student(name =request.json['name'],age = request.json['age'],grade =request.json['grade'],rollnumber= request.json['rollnumber'])
    db.session.add(student)
    db.session.commit()
    return {"id":student.id}

@app.route('/students/<id>', methods = ['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if student is None:
        return {"error":"Not Found"}
    student.name = request.json['name']
    student.age = request.json['age']
    student.grade = request.json['grade']
    student.rollnumber = request.json['rollnumber']
    db.session.commit()
    return {"message":"updated Successfully!"}

@app.route('/students/<id>', methods = ['PATCH'])
def patch_student(id):
    student = Student.query.get(id)
    if student is None:
        return {"error":"Not Found"}
    if "name" in request.json:
        student.name = request.json['name']
    if "age" in request.json:
        student.age = request.json['age']
    if "grade" in request.json:
        student.grade = request.json['grade']
    if "rollnumber" in request.json:
        student.rollnumber = request.json['rollnumber']
    db.session.commit()
    return {"message":"patched Successfully!"}


