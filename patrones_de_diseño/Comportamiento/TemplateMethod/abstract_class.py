from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print('La clase abstracta dice: Estoy haciendo la mayor parte del trabajo.')

    def base_operation2(self):
        print('La clase abstracta dice: Pero dejo que las subclases anulen algunas operaciones.')

    def base_operation3(self):
        print('La clase abstracta dice: Pero de todos modos estoy haciendo la mayor parte del trabajo.')

    @abstractmethod
    def required_operations1(self):
        pass

    @abstractmethod
    def required_operations2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass