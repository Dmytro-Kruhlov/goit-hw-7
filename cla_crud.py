import argparse


parser = argparse.ArgumentParser(description='CLA CRUD')
parser.add_argument('--action', "-a", help='Command: create, update, list, remove')
parser.add_argument('--model', "-m", help="Command: Teacher, Student, Discipline, ")
parser.add_argument('--name', "-n")
parser.add_argument('--id', "-id")

arguments = parser.parse_args()
print(arguments)
my_arg = vars(arguments)
print(my_arg)

action = my_arg.get('action')
model = my_arg.get('model')
name = my_arg.get('name')
id = my_arg.get("id")

def main():
    match action:



if __name__ == '__main__':
