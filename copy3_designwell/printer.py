from device_output import IDeviceOutput


class Printer(IDeviceOutput):

    @classmethod
    def write(cls, value):
        print('Printer: {}'.format(value))
