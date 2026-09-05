"""
Section 5 — Comparison + Final Application Demo
Topic: ORM vs SQL + Complete Demonstration

Resets the tables first so this always runs as a clean, self-contained
walkthrough regardless of what earlier sections left behind:

1. Create courses
2. Create students
3. Assign students to courses
4. Search students
5. Update a student
6. Delete a student
7. Display final database
"""

from models import db, Student, Course


def show_students(label):
    print(f"\n-- {label} --")
    for student in Student.select():
        course_name = student.course.name if student.course else "None"
        print(f"  {student.id}: {student.name}, age {student.age}, course: {course_name}")


def run():
    db.connect()
    db.drop_tables([Student, Course])
    db.create_tables([Course, Student])

    # 1. Create courses
    cs = Course.create(name="Computer Science")
    business = Course.create(name="Business")

    # 2. Create students
    Student.create(name="Tihara", age=23, email="tihara@email.com")
    Student.create(name="Tharushi", age=22, email="tharushi@email.com")
    Student.create(name="Kavindu", age=25, email="kavindu@email.com")

    # 3. Assign students to courses
    Student.update(course=cs).where(Student.name.in_(["Tihara", "Kavindu"])).execute()
    Student.update(course=business).where(Student.name == "Tharushi").execute()
    show_students("After creating students and assigning courses")

    # 4. Search students
    print("\n-- Search: students enrolled in Computer Science --")
    for student in cs.students:
        print(f"  {student.name}")

    # 5. Update a student
    student = Student.get(Student.name == "Tihara")
    student.age = 24
    student.save()
    show_students("After updating Tihara's age")

    # 6. Delete a student
    Student.delete().where(Student.name == "Kavindu").execute()
    show_students("After deleting Kavindu")

    # 7. Display final database
    show_students("Final database state")

    db.close()


if __name__ == "__main__":
    run()
