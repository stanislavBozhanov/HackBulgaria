while True:
    command = input('Enter command>')
    command = command.split(' ')
    orders = {}
    if command[0] == 'take':
        if command[1] in orders:
            orders[command[1]] += int(command[2])
            
