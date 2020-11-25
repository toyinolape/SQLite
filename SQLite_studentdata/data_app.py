import sqlite3


# Query the DB and Return all RECORDs
def show_all():
    # Connect to database
    conn = sqlite3.connect('student.db')

    # Create a cursor
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM students")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

# Add to new record
def add_one(first, last, email, course):
     # Connect to database
    conn = sqlite3.connect('student.db')

    # Create a cursor
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (?,?,?,?)",(first, last, email, course))

    conn.commit()
    conn.close()


def delete_one(id):
    # Connect to database
    conn = sqlite3.connect('student.db')

    # Create a cursor
    c = conn.cursor()
    c.execute("DELETE from students WHERE rowid=(?)",(id))

    conn.commit()
    conn.close()


def add_many(list):
     # Connect to database
    conn = sqlite3.connect('student.db')

    # Create a cursor
    c = conn.cursor()
    c.executemany("INSERT INTO students VALUES (?,?,?,?)",(list))

    conn.commit()
    conn.close()

def email_lookup(email):
    # Connect to database
    conn = sqlite3.connect('student.db')

    # Create a cursor
    c = conn.cursor()
    c.execute("SELECT rowid, * from students WHERE email =  (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()