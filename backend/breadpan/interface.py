from abc import ABCMeta, abstractmethod
from breadpan.usecase import UsecaseOutputPort
from breadpan.entity import Entity

class Presenter(UsecaseOutputPort):
    """IPresenter 
    
    """
    def __init__(self, output_port: UsecaseOutputPort):
        self.output = output_port.output

    @abstractmethod
    def ouput(self):
        """output
        Do any operation additionally.
        """
        pass
    


class Controller(metaclass=ABCMeta):
    """Interface of data controller class.

    """

    @abstractmethod
    def create(self, **kwargs) -> Presenter:
        pass

    @abstractmethod
    def read(self,  **kwargs) -> Presenter:
        pass

    @abstractmethod
    def update(self,  **kwargs) -> Presenter:
        pass

    @abstractmethod
    def delete(self,  **kwargs) -> Presenter:
        pass

