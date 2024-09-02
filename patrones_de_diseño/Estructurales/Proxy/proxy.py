from subject import Subject, RealSubject

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        else:
            return 'Proxy: Acceso Denegado'

    def check_access(self):
        print('Proxy: Comprobación del acceso antes de lanzar una solicitud real.')
        return True

    def log_access(self):
        print('Proxy: Registro de la hora de solicitud.')
