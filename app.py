from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from flask import render_template

app = Flask(__name__)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    db.collection('students').document(data['id']).set(data)
    return jsonify({"success": True, "message": "Student added successfully!"})

@app.route('/update_student', methods=['PUT'])
def update_student():
    data = request.json
    db.collection('students').document(data['id']).update(data)
    return jsonify({"success": True, "message": "Student updated successfully!"})

@app.route('/delete_student/<id>', methods=['DELETE'])
def delete_student(id):
    db.collection('students').document(id).delete()
    return jsonify({"success": True, "message": "Student deleted successfully!"})

@app.route('/search_student/<id>', methods=['GET'])
def search_student(id):
    student = db.collection('students').document(id).get()
    if student.exists:
        return jsonify({"success": True, "student": student.to_dict()})
    return jsonify({"success": False, "message": "Student not found!"})

@app.route('/view_students', methods=['GET'])
def view_students():
    students = db.collection('students').stream()
    student_data = {student.id: student.to_dict() for student in students}
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(debug=True)