from abc import ABC, abstractmethod

# Clase abstracta que difine la interfaz
# para todos los tipos de vehículos
class Vehicle(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Subclases de Veichle una representa un carro y la otra
# un camión, al igual las dos devuelven un mensaje
class Car(Vehicle):
    def __init__(self, model):
        self._model = model

    def deliver(self):
        return f"Auto {self._model} entregado"

class Truck(Vehicle):
    def __init__(self, model):
        self._model = model

    def deliver(self):
        return f"Camión {self._model} entregado"