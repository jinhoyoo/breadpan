from abc import *
from breadpan.entity import IEntity


class IDataAccessGateway(metaclass=ABCMeta):
    """Interface of data access class. 
    """
        
    @abstractmethod
    def create(self, entity: IEntity):
        pass

    @abstractmethod
    def read(self,  **kwargs) -> IEntity:
        pass

    @abstractmethod
    def update(self, entity: IEntity, **kwargs):
        pass

    @abstractmethod
    def delete(self,  entity: IEntity):
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
    __data_access = None

    def __init__( d : IDataAccessGateway):
        self.__data_access = d


    @abstractmethod
    def run(self):
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
    



