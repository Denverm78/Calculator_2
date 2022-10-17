import logger
import model
import view

def input_mode(enter):
    while True:
        a = input(enter)
        if a in ['1', '2']:
            return a
        else:
            view.error_value()

def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()


def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()


def operation():
    if model.ops == '+':
        model.total = model.first + model.second
    elif model.ops == '-':
        model.total = model.first - model.second
    elif model.ops == '*':
        model.total = model.first * model.second
    elif model.ops == '/':
        while model.second == 0:
            print('На ноль делить нельзя!')
            model.init_second()
        model.total = int(model.first / model.second)
    else:
        view.error_value()
    logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}')


def input_str(enter):
    str = input(enter)
    return str


def operation_with_string():
    model.my_str = model.my_str.strip().replace(" ", "")
    list = []
    dig =""
    for i in model.my_str:
        if i.isdigit():
            dig = dig+i
        else:
            list.append(dig)
            list.append(i)
            dig=""
    list.append(dig)
    
    i = 0
    while '*' in list or '/' in list:
        if list[i] == "*" or list[i] == '/':
            if list[i] == '*':
                list[i-1] = int(list[i-1]) * int(list[i+1])
                list.pop(i)
                list.pop(i)
                i = 0
            else:
                list[i-1] = int(list[i-1]) / int(list[i+1])
                list.pop(i)
                list.pop(i)
                i=0
        i += 1

    while '+' in list or '-' in list:
        if list[i] == "+" or list[i] == '-':
            if list[i] == '+':
                list[i-1] = int(list[i-1]) + int(list[i+1])
                list.pop(i)
                list.pop(i)
                i = 0
            else:
                list[i-1] = int(list[i-1]) - int(list[i+1])
                list.pop(i)
                list.pop(i)
                i=0
        i += 1
    logger.logger(f'{model.my_str} = {list[0]}')
    view.print_total_str(list[0])
    
    
