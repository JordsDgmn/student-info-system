from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from flask_mysqldb import MySQL

db = SQLAlchemy()

# Define your routes
# Import and register your blueprints
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ssis123@localhost/SSISv3'
    db.init_app(app)  # Initialize the SQLAlchemy app

    from app.routes.routes import index_route
    app.register_blueprint(index_route)

    from app.routes.college_route import college_bp
    app.register_blueprint(college_bp)

    from app.routes.course_route import course_bp
    app.register_blueprint(course_bp)

    from app.routes.student_route import student_bp
    app.register_blueprint(student_bp)

    return app



# from flask import Flask
# import mysql.connector
# #from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy

# # Add the SQLALCHEMY_DATABASE_URI configuration to your app
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ssis123@localhost/SSISv3'
# db = SQLAlchemy(app)

# # Define your models using SQLAlchemy
# class College(db.Model):
#     __tablename__ = 'college'
#     code = db.Column(db.String(10), primary_key=True)
#     name = db.Column(db.String(100))

# class Course(db.Model):
#     __tablename__ = 'course'
#     code = db.Column(db.String(10), primary_key=True)
#     name = db.Column(db.String(100))
#     college_code = db.Column(db.String(10), db.ForeignKey('college.code'))
#     college = db.relationship('College', backref='courses')

# class Student(db.Model):
#     __tablename__ = 'student'
#     id = db.Column(db.String(9), primary_key=True)
#     firstname = db.Column(db.String(20))
#     lastname = db.Column(db.String(20))
#     course_code = db.Column(db.String(10), db.ForeignKey('course.code'))
#     course = db.relationship('Course', backref='students')
#     year = db.Column(db.String(20))
#     gender = db.Column(db.String(10))
#     profile_pic_url = db.Column(db.String(255))
# # Define your routes
# app = Flask(__name__)

# # Import and register your blueprints
# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ssis123@localhost/SSISv3'
#     db.init_app(app)

#     from app.routes.routes import index_route
#     app.register_blueprint(index_route)

#     from app.routes.college_route import college_bp
#     app.register_blueprint(college_bp)

#     from app.routes.course_route import course_bp
#     app.register_blueprint(course_bp)

#     from app.routes.student_route import student_bp
#     app.register_blueprint(student_bp)

#     return app
