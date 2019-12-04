from abc import *
from breadpan.entity import Entity

class DataAccessGateway(metaclass=ABCMeta):
    """Interface of data access class. 
    """
        
    @abstractmethod
    def create(self, entity: Entity):
        pass

    @abstractmethod
    def read(self,  **kwargs):
        pass

    @abstractmethod
    def read_all(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self,  **kwargs):
        pass



class UsecaseInputPort(object):
    """Interface of use case input port.

    """
    data = {}

    def __init__(self):
        self.data = {}

    def input(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value



class UsecaseInteractor(UsecaseInputPort):
    """IUsecaseInteractor

    """
    @abstractmethod
    def run(self, data: DataAccessGateway):
        """operate
        Will return the class inherited from UsecaseOutputPort.
        """
        pass


class UsecaseOutputPort(metaclass=ABCMeta):
    """Interface of use case input port.

    """
    data = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value
    
