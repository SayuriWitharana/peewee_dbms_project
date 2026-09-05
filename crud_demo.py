"""
Section 3 — CRUD Operations
Topic: Creating, Reading, Updating and Deleting Data

Key line to say out loud during this section:
"We didn't write SQL, but Peewee generated and executed the SQL for us."
"""

from models import db, Student

db.connect()
db.create_tables([Student])


def show_students(label):
    print(f"\n-- {label} --")
    for student in Student.select():
        print(f"  {student.id}: {student.name}, age {student.age}, {student.email}")


def create_demo():
    Student.create(
        name="Tihara",
        age=23,
        email="tihara@email.com",
    )
    show_students("After CREATE")


def read_demo():
    students = Student.select()
    for student in students:
        print(student.name)


def update_demo():
    student = Student.get(Student.name == "Tihara")
    student.age = 24
    student.save()
    show_students("After UPDATE")


def delete_demo():
    Student.delete().where(
        Student.name == "Tihara"
    ).execute()
    show_students("After DELETE")


if __name__ == "__main__":
    create_demo()
    read_demo()
    update_demo()
    delete_demo()
    db.close()
