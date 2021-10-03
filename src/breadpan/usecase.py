from abc import *
from breadpan.entity import Entity

class UsecaseInputPort(object):
    """Interface of use case input port.

    """
    input = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.input[key] = value


class UsecaseInteractor(UsecaseInputPort):
    """IUsecaseInteractor

    """
    @abstractmethod
    def run(self,  **kwargs):
        """operate
        Will return the class inherited from UsecaseOutputPort.
        """
        pass


class UsecaseOutputPort(metaclass=ABCMeta):
    """Interface of use case input port.

    """
    output = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.output[key] = value
    
