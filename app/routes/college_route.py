from flask import Blueprint, render_template

college_bp = Blueprint('college', __name__)


@college_bp.route('/colleges')
def college_view():
    return render_template('colleges.html')