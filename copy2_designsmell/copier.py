from scanner import Scanner
from keyboard import Keyboard
from printer import Printer


class Copier(object):
    scanner_flag = True

    def copy(self):
        while True:
            input_value = Scanner.read() if self.scanner_flag else Keyboard.read()
            if not input_value:
                break
            Printer.write(input_value)
