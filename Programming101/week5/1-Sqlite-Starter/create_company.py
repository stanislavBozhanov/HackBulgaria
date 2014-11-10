import sqlite3

employees = [
    ('Ivan Ivanov', 5000, 10000, 'Software Developer'),
    ('Rado Rado', 500, 0, 'Technical Support Intern'),
    ('Ivo Ivo', 10000, 100000, 'CEO'),
    ('Petar Petrov', 3000, 1000, 'Marketing Manager'),
    ('Maria Georgieva', 8000, 10000, 'COO')
]

db = sqlite3.connect('employees.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees(id INTEGER  PRIMARY KEY ,name TEXT,
                 monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)''')
db.commit()

cursor.executemany(''' INSERT INTO employees(name, monthly_salary,
                     yearly_bonus, position) VALUES(?,?,?,?)''', employees)
db.commit()
