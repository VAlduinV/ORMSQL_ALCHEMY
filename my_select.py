from sqlalchemy.orm import Session
from my_models import Student, Group, Teacher, Subject, Grade  # import your models
from sqlalchemy import func

# create a session
session = Session()


# select_1: Find top 5 students with the highest average grade
def select_1():
    result = session.query(Student.name, func.avg(Grade.grade).label('average_grade')) \
        .join(Grade) \
        .group_by(Student.name) \
        .order_by(func.avg(Grade.grade).desc()) \
        .limit(5).all()
    return result


# add more functions as per the requirement...

# select_2: Find the student with the highest average grade for a particular subject
def select_2(subject_name):
    result = session.query(Student.name, func.avg(Grade.grade).label('average_grade')) \
        .join(Grade) \
        .join(Subject) \
        .filter(Subject.name == subject_name) \
        .group_by(Student.name) \
        .order_by(func.avg(Grade.grade).desc()) \
        .first()
    return result


# select_3: Find the average grade for groups for a particular subject
def select_3(subject_name):
    result = session.query(Group.name, func.avg(Grade.grade).label('average_grade')) \
        .join(Student) \
        .join(Grade) \
        .join(Subject) \
        .filter(Subject.name == subject_name) \
        .group_by(Group.name) \
        .all()
    return result


# select_4: Find the average grade in the stream (across all grades)
def select_4():
    result = session.query(func.avg(Grade.grade)).scalar()
    return result


# select_5: Find which courses a particular teacher teaches
def select_5(teacher_name):
    result = session.query(Subject.name) \
        .join(Teacher) \
        .filter(Teacher.name == teacher_name) \
        .all()
    return [r[0] for r in result]  # returning list of subject names


# continue with more select functions as per the requirement...
session.close()
