# importing libraries
from enum import unique
from flask import Flask, request, Response, jsonify
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true
# creating an instance of the flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initializing our database
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    student_id = db.Column(db.Integer,nullable=False )  # this is the primary key
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob=db.Column(db.String(20), nullable=False)
    amount_due=db.Column(db.Integer, nullable=False)
    # function to display the output as json
    def json(self):
        return {
                'id':self.id,
                'student_id': self.student_id, 
                'first_name': self.first_name,
                'last_name': self.last_name, 
                'dob': self.dob,
                'amount_due': self.amount_due
                
                }
    #function to add a new student to the database
    def add_student(ID,studentId, firstName, lastName,doB,amountDue):
        # creating an instance of our Student constructor
        new_student = Student(id=ID,student_id=studentId, first_name=firstName, last_name=lastName, dob=doB,amount_due=amountDue)
        db.session.add(new_student)  # add new Student to database session
        db.session.commit()  # commit changes to session
    #function to get all the students saved in the database
    def get_all_students():
        return [Student.json(student) for student in Student.query.all()]

    # function to get a student with a specific id from database
    # by using .first method
    def get_student(Id):
        return [Student.json(Student.query.filter_by(id=Id).first())]
    
    #function to update details of a student based on his Id
    def update_student(Id,studentId, firstName, lastName,doB,amountDue):

        student_for_update = Student.query.filter_by(id=Id).first()
        student_for_update.student_id = studentId
        student_for_update.first_name = firstName
        student_for_update.last_name = lastName
        student_for_update.dob = doB
        student_for_update.amount_due = amountDue
        db.session.commit()
    #function to delete a  student based on his Id
    def delete_student(Id):
        Student.query.filter_by(id=Id).delete()
        db.session.commit()  # commiting the new change to our database