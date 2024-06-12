from abc import ABC, abstractmethod, abstractproperty

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass

    @property
    @abstractmethod
    def valor(self):
        pass