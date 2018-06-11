from abc import ABC


class IDeviceOutput(ABC):

    @classmethod
    def write(cls):
        pass
