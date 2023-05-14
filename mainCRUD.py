import argparse
from sqlalchemy.orm import Session
from my_models import Teacher, Group  # import your models

# create a session
session = Session()


def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()


# add more create functions for other models...

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.name}")


def list_groups():
    groups = session.query(Group).all()
    for group in groups:
        print(f"ID: {group.id}, Name: {group.name}")


# add more list functions for other models...

def update_teacher(id, name):
    teacher = session.query(Teacher).get(id)
    if teacher is None:
        print(f"No teacher with ID {id} found.")
    else:
        teacher.name = name
        session.commit()


def update_group(id, name):
    group = session.query(Group).get(id)
    if group is None:
        print(f"No group with ID {id} found.")
    else:
        group.name = name
        session.commit()


# add more update functions for other models...

def remove_teacher(id):
    teacher = session.query(Teacher).get(id)
    if teacher is None:
        print(f"No teacher with ID {id} found.")
    else:
        session.delete(teacher)
        session.commit()


def remove_group(id):
    group = session.query(Group).get(id)
    if group is None:
        print(f"No group with ID {id} found.")
    else:
        session.delete(group)
        session.commit()


# add more remove functions for other models...

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action", help="CRUD action to be performed. (create, list, update, remove)")
parser.add_argument("-m", "--model", help="Model on which to perform the action. (Teacher, Group)")
parser.add_argument("-n", "--name", help="Name to be used with create or update action.")
parser.add_argument("-id", "--id", help="ID to be used with update or remove action.", type=int)

args = parser.parse_args()

if args.action == "create":
    if args.model == "Teacher":
        create_teacher(args.name)
    elif args.model == "Group":
        create_group(args.name)
    # add more models...

elif args.action == "list":
    if args.model == "Teacher":
        list_teachers()
    elif args.model == "Group":
        list_groups()
    # add more models...

elif args.action == "update":
    if args.model == "Teacher":
        update_teacher(args.id, args.name)
    elif args.model == "Group":
        update_group(args.id, args.name)
    # add more models...

elif args.action == "remove":
    if args.model == "Teacher":
        remove_teacher(args.id)
    elif args.model == "Group":
        remove_group(args.id)
    # add more models...

else:
    print("Invalid action.")

# don't forget to close the
session.close()
