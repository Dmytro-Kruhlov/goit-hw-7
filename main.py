import argparse
from commands import (
    add_student,
    add_group,
    add_grade,
    add_teacher,
    add_discipline,
    update_teacher,
    update_student,
    show_students,
    delete_student,
)

parser = argparse.ArgumentParser(description="CLA CRUD")
parser.add_argument("--action", "-a", help="Command: create, update, list, remove")
parser.add_argument("--model", "-m", help="Command: Teacher, Student, Discipline, ")
parser.add_argument("--name", "-n", nargs="+")
parser.add_argument("--id", "-id", nargs="+")

arguments = parser.parse_args()
print(arguments)
my_arg = vars(arguments)
print(my_arg)

action = my_arg.get("action")
model = my_arg.get("model")
name = my_arg.get("name")
if name:
    fullname = " ".join(name)

_id = my_arg.get("id")
if _id:
    id_1 = _id[0]
    if len(_id) > 1:
        id_2 = _id[1]


def main():
    match action:
        case "add":
            match model:
                case "Student":
                    add_student(fullname)
                case "Teacher":
                    add_teacher(fullname)
                case "Group":
                    add_group(name)
                case "Discipline":
                    add_discipline(name)
                case "Grade":
                    add_grade(id_1, id_2)
        case "update":
            match model:
                case "Student":
                    update_student(id_1, fullname, id_2)
                case "Teacher":
                    update_teacher(id_1, fullname)
        case "list":
            match model:
                case "Student":
                    show_students()
        case "delete":
            match model:
                case "Student":
                    delete_student(id_1)


if __name__ == "__main__":
    main()
