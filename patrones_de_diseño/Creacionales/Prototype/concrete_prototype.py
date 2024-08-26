import copy
from prototype import Prototype

# Subclase de 'Prototype'
class SystemConfigPrototype(Prototype):
    # Representa la configuración del sistema
    def __init__(self, configuration):
        self.configuration = configuration

    # Realiza una copia recursivamente
    def clone(self):
        return copy.deepcopy(self)