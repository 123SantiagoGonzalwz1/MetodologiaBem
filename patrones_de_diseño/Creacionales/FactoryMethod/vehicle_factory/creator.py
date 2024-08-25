from abc import ABC, abstractmethod
from product import Car, Truck

# Clase abstracta
class VehicleFactory(ABC):
    @abstractmethod
    # Método factory que será implementado por las subclases
    # que creara instancias de 'Vehicle'
    def get_vehicle(self, vehicle_type):
        pass