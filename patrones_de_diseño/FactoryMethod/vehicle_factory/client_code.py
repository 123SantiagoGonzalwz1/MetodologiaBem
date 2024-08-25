import sys
import os

# Agregue la ruta actual al PYTHONPATH porque no reconocía el archivo
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from concrete_factory import CarFactory, TruckFactory

# Utiliza la fábrica para crear un vehículo y
# luego lo impreme el resultado en el método 'get_vehicle'
def client_vehicle_code(factory, vehicle_type):
    vehicle = factory.get_vehicle(vehicle_type)
    print(vehicle.deliver())