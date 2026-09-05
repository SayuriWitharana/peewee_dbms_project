"""
Section 2 — Models and Tables
Topic: Mapping Python Classes -> Database Tables

Course is included here too since Section 4 (Queries and Relationships)
needs it — but when demoing Section 2, only talk through BaseModel and
Student. Introduce Course + the course field when you get to Section 4.

Student class     -> student table
name              -> name column
age               -> age column
Student object    -> a row in the table
"""

from peewee import Model, CharField, IntegerField, ForeignKeyField
from database import db


class BaseModel(Model):
    class Meta:
        database = db


class Course(BaseModel):
    name = CharField()


class Student(BaseModel):
    name = CharField()
    age = IntegerField()
    email = CharField()
    course = ForeignKeyField(Course, backref="students", null=True)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Course, Student])
    print("Tables created: course, student")
    db.close()
