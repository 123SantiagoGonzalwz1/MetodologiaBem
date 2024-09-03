from abstract_class import AbstractClass

class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print('ConcreteClass1 dice: Implementando operation1')

    def required_operations2(self):
        print('ConcreteClass1 dice: Implementando operation2')

class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        print('ConcreteClass2 dice: Implementando operation1')

    def required_operations2(self):
        print('ConcreteClass2 dice: Implementando operation2')

    def hook1(self):
        print('ConcreteClass2 dice: Anulando hook1')