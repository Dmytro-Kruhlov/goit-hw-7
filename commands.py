from sqlalchemy import select, update, delete
from src.db import session
from src.models import Student, Teacher, Group, Discipline, Grade
from random import choice, randint
from datetime import datetime


def add_student(name):
    group_ids = session.scalars(select(Group.id)).all()
    print(group_ids)
    new_student = Student(fullname=name, group_id=choice(group_ids))
    session.add(new_student)
    session.commit()
    return new_student


def add_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()
    return teacher


def add_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    return group


def add_discipline(name):
    teacher_ids = session.scalars(select(Teacher.id)).all()
    discipline = Discipline(name=name, teacher_id=choice(teacher_ids))
    session.add(discipline)
    session.commit()
    return discipline


def add_grade(student_id, dis_id):
    date = datetime.strftime(datetime.now().date(), "%Y-%m-%d")
    grade = Grade(
        grade=randint(1, 12), date_of=date, student_id=student_id, discipline_id=dis_id
    )
    session.add(grade)
    session.commit()
    return grade


def update_student(_id, name, gr_id):
    student = session.query(Student).filter(Student.id == _id)
    student.update({"fullname": name, "group_id": gr_id})
    session.commit()
    session.close()
    return student.one()


def update_teacher(_id, name):
    teacher = session.query(Teacher).filter(Teacher.id == _id)
    teacher.update({"fullname": name})
    session.commit()
    session.close()
    return teacher.one()


def show_students():
    print(session.scalars(select(Student.fullname)).all())


def delete_student(_id):
    r = session.query(Student).filter(Student.id == _id).delete()
    session.commit()
    session.close()
    return r


if __name__ == "__main__":
    delete_student(51)
