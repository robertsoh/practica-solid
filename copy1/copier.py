from keyboard import Keyboard
from printer import Printer


class Copier(object):

    def copy(self):
        while True:
            input_value = Keyboard.read()
            if not input_value:
                break
            Printer.write(input_value)
