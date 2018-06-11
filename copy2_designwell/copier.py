from printer import Printer


class Copier(object):

    def copy(self, device_input):
        while True:
            input_value = device_input.read()
            if not input_value:
                break
            Printer.write(input_value)
