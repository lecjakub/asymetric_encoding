from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self,key):
        self.key = key

    @abstractmethod
    def encode(self,data):
        raise NotImplementedError

    @abstractmethod
    def decode(self,data):
        raise NotImplementedError