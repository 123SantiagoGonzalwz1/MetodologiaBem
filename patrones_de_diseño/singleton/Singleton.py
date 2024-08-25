# Singleton
class Singleton:
    _instances = {} # Almacena las instancias de la clase

    # Crear una nueva instancia de la clase
    # con el método new
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)

        return cls._instances[cls]

# Creamos dos objetos que serían la misma instancia
objt1 = Singleton()
objt2 = Singleton()

# Comparamos y como son la misma instancia saldrá siempre 'True'
print(objt1 is objt2)

# Ejemplo Singleton / Connection DB
import sqlite3

# La clase de conexión hereda del patrón singleton
class DatabaseConnection(Singleton):
    connection = None # Aquí se almacenara la conexión a la DB

    # Inicializa la conexión
    def __init__(self):
        if self.connection is None:
            self.connection = sqlite3.connect("users.db")
    
    # Recibe una consulta, crea un cursor de la conexión existente
    # ejecuta la consulta y realiza un 'commit' guardando los
    # cambios en la DB
    def execute_query(self, Query):
        cursor = self.connection.cursor()
        cursor.execute(Query)
        self.connection.commit()

    # Método que termina la conexión
    def close(self):
        self.connection.close()

# Creamos una tabla e insertamos datos
db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Santiago')")

# Comparamos y como es la misma instancia siempre devolverá 'True'
print(db1 is db2)

# Llamamos a close para cerrar la conexión
# solo con un llamado basta
db1.close()
db2.close()
