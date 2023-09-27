from sqlalchemy import func, desc, select, and_

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def select_one():
    result = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


def select_two(discipline_id: int):
    r = (
        session.query(
            Discipline.name,
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.id, Discipline.name)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return r


def select_three(discipline_id):
    r = (
        session.query(
            Discipline.name,
            Group.name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(Discipline.id == discipline_id)
        .group_by(Discipline.name, Group.name)
        .order_by(desc("avg_grade"))
        .all()
    )

    return r


def select_four():
    r = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .all()
    )
    return r


def select_five(teacher_id):
    r = (
        session.query(
            Teacher.fullname,
            Discipline.name
        )
        .select_from(Discipline)
        .join(Teacher)
        .filter(Discipline.teacher_id == teacher_id)
        .order_by(desc(Teacher.fullname))
        .all()
    )
    
    return r


def select_six(group_id):
    r = (
        session.query(
            Student.fullname,
            Group.name
        )
        .select_from(Student)
        .join(Group)
        .filter(Group.id == group_id)
        .all()
    )
    
    return r


def select_seven():
    r = (
        session.query(Student.fullname, Group.name)
        .select_from(Student)
        .join(Group)
        .filter(Group.id == group_id)
        .all()
    )
    
    return r
def select_twelve(discipline_id, group_id):
    subquery = (
        select(Grade.date_of)
        .join(Student)
        .join(Group)
        .where(and_(Grade.discipline_id == discipline_id, Group.id == group_id))
        .order_by(desc(Grade.date_of))
        .limit(1)
        .scalar_subquery()
    )

    r = (
        session.query(
            Discipline.name, Student.fullname, Group.name, Grade.date_of, Grade.grade
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(
            and_(
                Discipline.id == discipline_id,
                Group.id == group_id,
                Grade.date_of == subquery,
            )
        )
        .order_by(desc(Grade.date_of))
        .all()
    )
    return r


if __name__ == "__main__":
    # print(select_one())
    print(select_two(1))
    # print(select_three(1))
    # print(select_four()[0][0])
    # print(select_five(5))
    # print(select_six(1))


    #print(select_twelve(1, 2))