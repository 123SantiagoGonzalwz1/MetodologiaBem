from abc import ABC, abstractmethod

class Memento(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def get_date(self):
        pass