from flask import Blueprint, render_template
from app.models.studentModel import StudentModel

student_bp = Blueprint('student', __name__)
student_model = StudentModel


@student_bp.route('/students', methods=["GET", "POST"])
def student_view():
    students = StudentModel.query.all()  # Fetch all students from the database
    return render_template('students.html', students=students)