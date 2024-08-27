from component import FileSystemComponent

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f'Archivo: {self.name}')