from abc import *
from breadpan.entity import IEntity

class IDataAccessGateway(metaclass=ABCMeta):
    """Interface of data access class. 
    """
        
    @abstractmethod
    def create(self, entity: IEntity):
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



class IUsecaseInputPort(object):
    """Interface of use case input port.

    """
    data = {}

    def __init__(self):
        self.data = {}

    def input(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value



class IUsecaseInteractor(IUsecaseInputPort):
    """IUsecaseInteractor

    """
    @abstractmethod
    def run(self, data: IDataAccessGateway):
        """operate
        Will return the class inherited from IUsecaseOutputPort.
        """
        pass


class IUsecaseOutputPort(metaclass=ABCMeta):
    """Interface of use case input port.

    """
    data = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value
    



