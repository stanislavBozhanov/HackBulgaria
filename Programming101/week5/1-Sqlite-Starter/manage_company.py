import sqlite3

connection = sqlite3.connect('employees.db')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

while True:
    command = input('command>')
    if command == 'list_employees':
        result = cursor.execute('SELECT name, position FROM employees')
        for row in result:
            print('{name} - {position}'.format(**row))
    elif command == 'monthly_spending':
        result = cursor.execute('SELECT SUM(monthly_salary) AS sum FROM employees;').fetchone()
        print('The company is spending {sum} every month!'.format(**result))
    elif command == 'yearly_spending':
        result = cursor.execute('SELECT SUM(monthly_salary * 12 + yearly_bonus) AS sum FROM employees;').fetchone()
        print('The company is spending {sum} every year!'.format(**result))
    elif command == 'add_employee':
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
    connection.commit()
