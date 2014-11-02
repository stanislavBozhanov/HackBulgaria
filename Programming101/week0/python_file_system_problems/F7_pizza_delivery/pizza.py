import os
from time import time
from datetime import datetime

orders = {}


def get_stamp():
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    return stamp


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
    status = ""
    for order in orders:
        status += "{} - {:.2f}\n".format(order, orders[order])
    return status


def save():
    stamp = get_stamp()
    filename = stamp + '.txt'
    content = status_command(orders)
    f = open(filename, 'w')
    f.write(content)
    f.close()


def list():
    order_list = {}
    path = os.getcwd()
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            order_list[counter] = filename
        counter += 1
    return order_list
