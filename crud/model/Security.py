

from abc import ABC,abstractmethod


class Security(ABC):

    @abstractmethod
    def encrypt(self):
        pass
    @abstractmethod
    def dcrypt(self,passwd):
        pass