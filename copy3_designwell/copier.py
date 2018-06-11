from printer import Printer


class Copier(object):

    def copy(self, device_input, device_output):
        while True:
            input_value = device_input.read()
            if not input_value:
                break
            device_output.write(input_value)
