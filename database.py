"""
Section 1 — Introduction + Database Setup
Topic: What is ORM and what is Peewee?

This is the one place the SQLite connection is created. Every other
file imports `db` from here instead of creating its own connection.
"""

from peewee import SqliteDatabase

db = SqliteDatabase("student.db")


if __name__ == "__main__":
    db.connect()
    print("Connected to SQLite database: student.db")
    print("Peewee will translate Python model calls into SQL statements")
    print("and run them against this database file.")
    db.close()
