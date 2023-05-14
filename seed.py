from faker import Faker
from sqlalchemy.orm import Session
from my_models import Student, Group, Teacher, Subject, Grade  # import your models

fake = Faker()

# create a session
session = Session()

# create groups
for _ in range(3):
    group = Group(name=fake.word())
    session.add(group)

session.commit()

# create students and add them to groups
for _ in range(50):
    student = Student(name=fake.name(), group_id=fake.random_int(min=1, max=3))
    session.add(student)

session.commit()

# add more data as per the requirement...

# don't forget to close the session at the end
session.close()
