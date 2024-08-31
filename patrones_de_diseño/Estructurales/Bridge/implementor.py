from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_shape(self, shape):
        pass

class VectorRenderer(Renderer):
    def render_shape(self, shape):
        print(f'Dibujando un {shape} con líneas')

class RasterRenderer(Renderer):
    def render_shape(self, shape):
        print(f'Dibujando un {shape} con píxeles')