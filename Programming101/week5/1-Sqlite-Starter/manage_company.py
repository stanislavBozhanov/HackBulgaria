import sqlite3

connection = sqlite3.connect('employees.db')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

while True:
    command = input('command>')
    command = command.split()
    if command[0] == 'list_employees':
        result = cursor.execute('SELECT name, position FROM employees')
        for row in result:
            print('{name} - {position}'.format(**row))
    elif command[0] == 'monthly_spending':
        result = cursor.execute('SELECT SUM(monthly_salary) AS sum FROM employees;').fetchone()
        print('The company is spending {sum} every month!'.format(**result))
    elif command[0] == 'yearly_spending':
        result = cursor.execute('SELECT SUM(monthly_salary * 12 + yearly_bonus) AS sum FROM employees;').fetchone()
        print('The company is spending {sum} every year!'.format(**result))
    elif command[0] == 'add_employee':
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        cursor.execute('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
        connection.commit()
    elif command[0] == 'delete_employee':
        number = int(command[1])
        cursor.execute('''DELETE FROM employees WHERE id = ? ''', (number,))
        connection.commit()
    elif command[0] == 'update':
        number = int(command[1])
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        cursor.execute('''UPDATE employees SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
                    WHERE id = ? ''', (name, monthly_salary, yearly_bonus, position, number))
        connection.commit()
    elif command == 'finish':
        connection.close()
    else:
        print('Wrong command!')
