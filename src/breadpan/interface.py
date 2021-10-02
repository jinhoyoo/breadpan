from abc import ABCMeta, abstractmethod
from breadpan.usecase import UsecaseOutputPort
from breadpan.entity import Entity

class Presenter(UsecaseOutputPort):
    """IPresenter 
    """
    def __init__(self, output_port: UsecaseOutputPort):
        self.output = output_port.output

    def show(self) -> dict:
        """show the data to outer. 
        
        Implement any operation to convert data to expose if you need. 
        Or retruen data as we got from the UsecaseOutputPort. 
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

