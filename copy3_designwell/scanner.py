from device_input import IDeviceInput


class Scanner(IDeviceInput):

    def read(self):
        return input('Scanner - Enter String: ')
