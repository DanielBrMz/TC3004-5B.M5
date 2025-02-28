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


# Productos concretos para Windows
class BotonWindows(Boton):
    def __init__(self, texto):
        self.texto = texto
    
    def renderizar(self):
        print(f"Renderizando botón de Windows con texto: {self.texto}")
    
    def onClick(self):
        print(f"Click en botón de Windows: {self.texto}")


class VentanaWindows(Ventana):
    def __init__(self, titulo):
        self.titulo = titulo
    
    def renderizar(self):
        print(f"Renderizando ventana de Windows con título: {self.titulo}")
    
    def cerrar(self):
        print(f"Cerrando ventana de Windows: {self.titulo}")


# Productos concretos para Mac
class BotonMac(Boton):
    def __init__(self, texto):
        self.texto = texto
    
    def renderizar(self):
        print(f"Renderizando botón de Mac con texto: {self.texto}")
    
    def onClick(self):
        print(f"Click en botón de Mac: {self.texto}")


class VentanaMac(Ventana):
    def __init__(self, titulo):
        self.titulo = titulo
    
    def renderizar(self):
        print(f"Renderizando ventana de Mac con título: {self.titulo}")
    
    def cerrar(self):
        print(f"Cerrando ventana de Mac: {self.titulo}")


# Fábricas concretas
class WindowsFactory(UIFactory):
    def crear_boton(self, texto="OK"):
        return BotonWindows(texto)
    
    def crear_ventana(self, titulo="Ventana de Windows"):
        return VentanaWindows(titulo)


class MacFactory(UIFactory):
    def crear_boton(self, texto="OK"):
        return BotonMac(texto)
    
    def crear_ventana(self, titulo="Ventana de Mac"):
        return VentanaMac(titulo)


# Cliente que usa la fábrica
def crear_ui(factory):
    boton = factory.crear_boton("Aceptar")
    ventana = factory.crear_ventana("Aplicación Demo")
    
    # Usamos los productos
    ventana.renderizar()
    boton.renderizar()
    boton.onClick()
    ventana.cerrar()


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración para Windows
    print("=== Creando UI para Windows ===")
    windows_factory = WindowsFactory()
    crear_ui(windows_factory)
    
    print("\n=== Creando UI para Mac ===")
    mac_factory = MacFactory()
    crear_ui(mac_factory)