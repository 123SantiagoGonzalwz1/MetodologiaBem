from mediator import Mediator

class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator