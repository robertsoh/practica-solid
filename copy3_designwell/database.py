from device_output import IDeviceOutput


class Database(IDeviceOutput):

    @classmethod
    def write(cls, value):
        print('Database: {}'.format(value))