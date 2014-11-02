orders = {}


def input():
    return input('Enter command>')


def get_command(command):
    commands = ['take', 'status', 'save', 'list', 'load', 'finish']
    command = command.split(' ')
    if command[0] in commands:
        return command
    else:
        raise ValueError('Wrong command')


def take_command(command, orders):
    if command[1] in orders:
        orders[command[1]] += float(command[2])
    else:
        orders[command[1]] = float(command[2])
    return orders


def status_command(orders):
    for order in orders:
        print("{} - {:.2f}".format(order, orders[order]))
