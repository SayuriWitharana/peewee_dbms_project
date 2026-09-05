# Peewee ORM Demo — Student Management System

Codebase for the "ORM (Peewee)" presentation, structured to follow the
5-section flow in `Adv DBMS.md`. Each section has its own file so you
can run/open them one at a time as you talk through them.

```
Python Classes
      |
   Peewee ORM
      |
  SQLite DB
      |
 Tables / Rows
```

## Setup

These steps are for Windows PowerShell. If `python` isn't recognized
(it opens the Microsoft Store instead), use the `py` launcher as shown
below — it comes with the standard Python installer.

1. Create a virtual environment:
   ```
   py -3 -m venv .venv
   ```

2. Activate it:
   ```
   .\.venv\Scripts\Activate.ps1
   ```
   If you get an error saying script execution is disabled, run this
   once (allows locally-created scripts for your user account only,
   still blocks unsigned scripts from the internet):
   ```
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```
   Then retry the activate command. Your prompt should now start with
   `(.venv)`.

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

If you'd rather not activate the venv at all, you can skip step 2 and
just run scripts directly with `.\.venv\Scripts\python.exe <file>.py`
and `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.

## Files (in presentation order)

1. `database.py` — **Intro + Database Setup.** Just the SQLite
   connection (`db = SqliteDatabase("student.db")`). Run it to show
   Peewee connecting to the database.

2. `models.py` — **Models and Tables.** Defines `Student` (name, age,
   email) and `Course`. When covering this section, only talk through
   `BaseModel` and `Student` — introduce `Course` and the `course`
   field later, in section 4. Run it to create the tables.

3. `crud_demo.py` — **CRUD Operations.** Create / Read / Update / Delete
   on `Student`, printing the table's contents after each step so you
   can show the data changing. Talking point: "We didn't write SQL, but
   Peewee generated and executed the SQL for us."

4. `queries_relationships_demo.py` — **Queries and Relationships.**
   Filtering (`.where(...)`), sorting (`.order_by(...)`), and the
   `Course` <-> `Student` foreign key relationship (both directions:
   `student.course` and `course.students`).

5. `final_demo.py` — **Comparison + Final Application Demo.** A
   self-contained run of the full flow: create courses -> create
   students -> assign students to courses -> search -> update -> delete
   -> display final database. It resets the tables at the start, so run
   it standalone as the closing demo regardless of what earlier
   sections left in `student.db`.

`reset_db.py` is a small utility (not part of the presentation) that
deletes `student.db` so you can rehearse a section from a clean slate.

## Running a section

```
python database.py
python models.py
python crud_demo.py
python queries_relationships_demo.py
python final_demo.py
```

Run `python reset_db.py` between rehearsals if you want a clean
database, or just delete `student.db` yourself.

## Talking points for the wrap-up (Section 5)

- **Advantages of ORM:** less raw SQL, reads like normal Python,
  harder to make SQL-injection/syntax mistakes, faster to write CRUD
  code, database-agnostic (Peewee also supports MySQL/PostgreSQL).
- **Disadvantages:** another abstraction layer to learn, less control
  over exact SQL generated, can be less efficient for very complex
  queries, still need to understand SQL/relational concepts underneath.
- **When to use it:** typical CRUD-heavy apps, prototypes, small-to-
  medium projects. **When not to:** highly performance-tuned queries,
  complex reporting/analytics SQL, or when you need full control over
  exact query plans.
