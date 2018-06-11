from device_input import IDeviceInput


class Keyboard(IDeviceInput):

    @classmethod
    def read(cls):
        return input('Keyboard - Enter String: ')
