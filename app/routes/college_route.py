from flask import Blueprint, render_template
from app.models.collegeModel import CollegeModel
from app import mysql

college_bp = Blueprint('college', __name__)

@college_bp.route('/colleges')
def college_view():
    return render_template('colleges.html')
