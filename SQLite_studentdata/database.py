# import dependency
import sqlite3

# Connect database
conn = sqlite3.connect('student.db')

# Create cursor
c = conn.cursor()

#c.execute('DROP TABLE students')
# Create student table
c.execute("""CREATE TABLE students(
                    first_name text,
                    last_name text,
                    email text,
                    course text
)""")

# Insert values into table
students_list = [('Josiah', 'Jovido', 'josiahjovido@gmail.com', 'DataScience'),
                 ('Toyin', 'Olape', 'toyinolape@gmail.com', 'DataScience'),
                 ('Mayowa', 'Kolawole', 'mayowakola@gmail.com', 'DataScience'),
                 ('Paul', 'Omikunle', 'paulomikunle@gmail.com', 'DataScience'),
                 ('Edun', 'Etinosa', 'edunetinosa@gmail.com', 'DataScience'),
                 ('Alex', 'Alexander', 'alexal@gmail.com', 'DataScience'),
                 ('Ifeanyi', 'Akawi', 'ifeanyiakawi@gmail.com', 'DataScience'),
                 ('Uso', 'Ikiliagwu', 'usoikili@gmail.com', 'DataScience'),
                 ('Ayodeni', 'Sanya', 'ayodeni@yahoo.com', 'Software'),
                 ('Melissa', 'Davids', 'melissadavis@yahoo.com', 'Software'),
                 ('Idogho', 'Louis', 'idogholew@yahoo.com', 'Software'),
                 ('Erons', 'Emma', 'eronsemma@yahoo.com', 'Software'),
                 ('Victory', 'Gold', 'victorygold@yahoo.com', 'Software'),
                 ('Tems', 'Teni', 'temsteni@yahoo.com', 'Software')
]

c.executemany("INSERT INTO students VALUES(?, ?, ?, ?)", students_list)

print('Command executed successfully...')

# Commit command
conn.commit()

# Close the connection
conn.close()