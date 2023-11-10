from app import db


class StudentModel(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.String(9), primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    course_code = db.Column(db.String(10), db.ForeignKey('course.code'), nullable=False)
    college_code = db.Column(db.String(45), nullable=False)
    year = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    profile_pic_url = db.Column(db.String(255))

    @classmethod
    def create_student(cls, id, firstname, lastname, course_code, college_code, year, gender):
        try:
            new_student = cls(
                id=id,
                firstname=firstname,
                lastname=lastname,
                course_code=course_code,
                college_code=college_code,
                year=year,
                gender=gender
            )
            db.session.add(new_student)
            db.session.commit()
            return "Student created successfully"
        except Exception as e:
            return f"Failed to create student: {str(e)}"

    @classmethod
    def get_students(cls, page_size: int, page_number: int):
        print(page_size, page_number)
        offset = (page_number - 1) * page_size
        try:
            from app.models.courseModel import CourseModel
            from app.models.collegeModel import CollegeModel

            course = CourseModel()
            college = CollegeModel()

            results = db.session.query(cls, course, college).filter(cls.course_code == course.code, cls.college_code == college.code).with_entities(
                cls.id, cls.firstname, cls.lastname,
                cls.course_code, cls.college_code, cls.year, cls.gender, cls.profile_pic_url,
                course.name.label('course_name'), course.code.label('course_code'),
                college.name.label('college_name'), college.code.label('college_code')
            ).limit(page_size).offset(offset).all()

            total_count = cls.query.count()
            has_prev = offset > 0
            has_next = (offset + page_size) < total_count

            return {
                'results': results,
                'total_count': total_count,
                'has_prev': has_prev,
                'has_next': has_next
            }
        except Exception as e:
            return f"Failed to retrieve students: {str(e)}"


# db = SQLAlchemy()

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

# class student(db.Model):
#     __tablename__ = 'student'
#     id = db.Column(db.String(9), primary_key=True)
#     firstname = db.Column(db.String(20))
#     lastname = db.Column(db.String(20))
#     course_code = db.Column(db.String(10), db.ForeignKey('course.code'))
#     course = db.relationship('Course', backref='students')
#     year = db.Column(db.String(20))
#     gender = db.Column(db.String(10))
#     profile_pic_url = db.Column(db.String(255))



