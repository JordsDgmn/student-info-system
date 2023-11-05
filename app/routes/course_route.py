from flask import Blueprint, render_template

course_bp = Blueprint('course', __name__)


@course_bp.route('/courses')
def course_view():
    return render_template('courses.html')