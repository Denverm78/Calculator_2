import controller
import model
import view

model.init_mode()
if model.mode == '1':
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total
else:
    model.init_str()
    controller.operation_with_string()

