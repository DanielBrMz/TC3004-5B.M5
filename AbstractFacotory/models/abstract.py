from abc import ABC, abstractmethod

# Productos abstractos
class Boton(ABC):
    @abstractmethod
    def renderizar(self):
        pass
    
    @abstractmethod
    def onClick(self):
        pass


class Ventana(ABC):
    @abstractmethod
    def renderizar(self):
        pass
    
    @abstractmethod
    def cerrar(self):
        pass


# Fábrica abstracta
class UIFactory(ABC):
    @abstractmethod
    def crear_boton(self):
        pass
    
    @abstractmethod
    def crear_ventana(self):
        pass