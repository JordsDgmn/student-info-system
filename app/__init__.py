from flask import Flask

# import mysql.connector
# from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy






def create_app():
    app = Flask(__name__)
   # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ssis123@localhost/SSISv3'
    from app.routes.routes import index_route
    app.register_blueprint(index_route)
        
        
        
    from app.routes.college_route import college_bp
    app.register_blueprint(college_bp)
    
    from app.routes.course_route import course_bp
    app.register_blueprint(course_bp)
    
    from app.routes.student_route import student_bp
    app.register_blueprint(student_bp)
        
    return app 