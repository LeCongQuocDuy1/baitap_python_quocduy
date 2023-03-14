from abc import ABC, abstractmethod


class IBaseDAO(ABC):
    @abstractmethod
    def insert(self, model):
        pass

    @abstractmethod
    def update(self, model):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def getById(self, id):
        pass

    @abstractmethod
    def getAll(self):
        pass
