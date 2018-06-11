from abc import ABC


class IDeviceInput(ABC):

    @classmethod
    def read(cls):
        pass
