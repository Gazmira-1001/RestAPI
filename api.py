from student import *

@app.route('/student', methods=['GET'])
def get_students():
    return jsonify({'All Students': Student.get_all_students()})

# route to get student by id
@app.route('/student/<int:Id>', methods=['GET'])
def get_student(Id):
    return_value = Student.get_student(Id)
    return jsonify(return_value)
# route to add new studnet
@app.route('/student', methods=['POST'])
def add_student():
    request_data = request.get_json()  # getting data from client
    Student.add_student(request_data["id"],request_data["student_id"], request_data["first_name"],
                    request_data["last_name"], request_data["dob"], request_data["amount_due"])
    response = Response("Student added", 201, mimetype='application/json')
    return response

# route to update student with PUT method
@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    request_data = request.get_json()
    Student.update_student(id, request_data['student_id'], request_data['first_name'], request_data['last_name'], request_data['dob'], request_data['amount_due'])
    response = Response("Student Updated", status=200, mimetype='application/json')
    return response
# route to delete a student using the DELETE method
@app.route('/student/<int:id>', methods=['DELETE'])
def deletestudent(id):
    #a calling to the function to delete student from database
    Student.delete_student(id)
    response = Response("Student Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1111, debug=True)