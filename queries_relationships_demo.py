"""
Section 4 — Queries and Relationships
Topic: More Advanced ORM Features

Course
---------
id
name
   ^
   |
Student
---------
id
name
course_id
"""

from models import db, Student, Course

db.connect()
db.create_tables([Course, Student])


def filtering_and_sorting_demo():
    Student.create(name="Amaya", age=21, email="amaya@email.com")
    Student.create(name="Kavindu", age=25, email="kavindu@email.com")

    print("\n-- Filtering: Student.select().where(Student.age > 20) --")
    for student in Student.select().where(Student.age > 20):
        print(f"  {student.name}, age {student.age}")

    print("\n-- Sorting: Student.select().order_by(Student.name) --")
    for student in Student.select().order_by(Student.name):
        print(f"  {student.name}")


def relationships_demo():
    course = Course.create(name="Computer Science")
    student = Student.create(
        name="Nethmi", age=22, email="nethmi@email.com", course=course
    )

    print("\n-- Following the relationship: student -> course --")
    print(f"  {student.name} is enrolled in {student.course.name}")

    print("\n-- Following the relationship: course -> students (backref) --")
    for s in course.students:
        print(f"  {s.name}")


if __name__ == "__main__":
    filtering_and_sorting_demo()
    relationships_demo()
    db.close()
