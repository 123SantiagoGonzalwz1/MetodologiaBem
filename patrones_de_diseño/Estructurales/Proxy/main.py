from subject import Subject, RealSubject
from proxy import Proxy

def client_code(subject: Subject):
    print(subject.request())

if __name__ == "__main__":
    print('Cliente: Ejecutando el código cliente con un sujeto real:')
    real_subject = RealSubject()
    client_code(real_subject)

    print('\nCliente: Ejecutar el mismo código de cliente con un proxy:')
    proxy = Proxy(real_subject)
    client_code(proxy)