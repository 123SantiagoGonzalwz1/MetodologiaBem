from abc import ABC, abstractmethod

class SupportHandler(ABC):
    def __init__(self, next_handler):
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, request):
        pass

class LevelOneSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request.level == 1:
            print('El soporte de nivel uno a resuelto el problema.')
        else:
            self._next_handler.handle_request(request)

class LevelTwoSupportHandler(SupportHandler):
    def handle_request(self, request):
        if request.level == 2:
            print('El soporte de nivel dos a resuelto el problema.')
        else:
            self._next_handler.handle_request(request)

