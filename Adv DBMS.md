## **Suggested Project**

Build a small **Student Management System** using **Python \+ Peewee \+ SQLite**.

You can demonstrate:

Python Classes  
      ↓  
    Peewee ORM  
      ↓  
   SQLite DB  
      ↓  
 Tables / Rows

This gives you enough material to demonstrate the main ORM concepts.

### **👩‍💻 Member 1 — Introduction \+ Database Setup**

**Topic: What is ORM and what is Peewee?**

Responsibilities:

* Explain what ORM means  
* Explain why ORM is used  
* Explain Peewee  
* Explain the difference between:  
  * Traditional SQL  
  * ORM  
* Set up the SQLite database  
* Connect Peewee to the database

Example:

from peewee import \*

db \= SqliteDatabase("student.db")

**Demo:**  
Show the database connection and explain how Peewee communicates with SQLite.

---

### **👩‍💻 Member 2 — Models and Tables**

**Topic: Mapping Python Classes → Database Tables**

This person should explain the **core ORM concept**.

Responsibilities:

* Create Peewee models  
* Explain fields  
* Explain primary keys  
* Explain how classes become tables

Example:

class Student(Model):  
    name \= CharField()  
    age \= IntegerField()  
    email \= CharField()

    class Meta:  
        database \= db

Explain:

Student class     → Student table  
name              → name column  
age               → age column  
Student object    → database row

**Demo:**  
Create the tables:

db.create\_tables(\[Student\])

Then show the resulting database table.

---

### **👨‍💻 Member 3 — CRUD Operations**

**Topic: Creating, Reading, Updating and Deleting Data**

This person gets one of the most important sections.

Responsibilities:

### **Create**

Student.create(  
    name="Tihara",  
    age=23,  
    email="tihara@email.com"  
)

### **Read**

students \= Student.select()

for student in students:  
    print(student.name)

### **Update**

student \= Student.get(Student.name \== "Tihara")  
student.age \= 24  
student.save()

### **Delete**

Student.delete().where(  
    Student.name \== "Tihara"  
).execute()

**Demo:**

Show the data changing in the database after each operation.

This is a good section for demonstrating:

> "We didn't write SQL, but Peewee generated/executed the SQL for us."

---

### **👩‍💻 Member 4 — Queries and Relationships**

**Topic: More Advanced ORM Features**

This member can demonstrate that ORM isn't just for basic CRUD.

Responsibilities:

* Filtering  
* Sorting  
* Selecting specific records  
* Foreign keys  
* Relationships between tables

For example, create:

class Course(Model):  
    name \= CharField()

class Student(Model):  
    name \= CharField()  
    course \= ForeignKeyField(Course)

Now you have:

Course  
\---------  
id  
name  
   ↑  
   |  
   |  
Student  
\---------  
id  
name  
course\_id

Then demonstrate:

Student.select().where(  
    Student.age \> 20  
)

And perhaps:

Student.select().order\_by(Student.name)

**Demo:**

Show how Peewee handles the relationship between `Student` and `Course`.

---

### **👨‍💻 Member 5 — Comparison \+ Final Application Demo**

**Topic: ORM vs SQL \+ Complete Demonstration**

This person ties everything together.

Responsibilities:

* Explain advantages of ORM  
* Explain disadvantages  
* Compare Peewee with traditional SQL  
* Explain when ORM should/shouldn't be used  
* Run the **complete application demo**

For example, demonstrate a simple flow:

1\. Create courses  
       ↓  
2\. Create students  
       ↓  
3\. Assign students to courses  
       ↓  
4\. Search students  
       ↓  
5\. Update student  
       ↓  
6\. Delete student  
       ↓  
7\. Display final database

This makes the presentation feel like a **real application**, rather than simply showing code snippets.

