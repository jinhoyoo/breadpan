from abc import ABCMeta, abstractmethod
from breadpan.usecase import IUsecaseOutputPort
from breadpan.entity import IEntity

class IPresenter(IUsecaseOutputPort):
    """IPresenter 
    
    """
    def __init__(self, output_port: IUsecaseOutputPort):
        self.data = output_port.data

    @abstractmethod
    def ouput(self):
        """output
        Do any operation additionally.
        """
        pass
    


class IController(metaclass=ABCMeta):
    """Interface of data controller class.

    """

    @abstractmethod
    def create(self, **kwargs) -> IPresenter:
        pass

    @abstractmethod
    def read(self,  **kwargs) -> IPresenter:
        pass

    @abstractmethod
    def update(self,  **kwargs) -> IPresenter:
        pass

    @abstractmethod
    def delete(self,  **kwargs) -> IPresenter:
        pass

