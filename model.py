import controller
import view

first = 0
second = 0
ops = ''
total = 0
mode = ''

def init_mode():
    global mode
    mode = controller.input_mode("Введите режим работы: '1' - посимвольный, '2' - строчный: ")


def init_first():
    global first
    first = controller.input_integer('Введите число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True

def init_str():
    global my_str
    my_str = controller.input_str('Введите строку примера: ')
    
    
    