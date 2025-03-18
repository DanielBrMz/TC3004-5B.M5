from abc import ABC, abstractmethod

class Bebida(ABC):
    """Interfaz abstracta para todas las bebidas"""
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """Retorna la descripción de la bebida"""
        pass
    
    @abstractmethod
    def obtener_costo(self) -> float:
        """Retorna el costo de la bebida"""
        pass


class Espresso(Bebida):
    """Bebida base: Espresso"""
    
    def obtener_descripcion(self) -> str:
        return "Espresso"
    
    def obtener_costo(self) -> float:
        return 1.99


class Americano(Bebida):
    """Bebida base: Americano"""
    
    def obtener_descripcion(self) -> str:
        return "Americano"
    
    def obtener_costo(self) -> float:
        return 1.50


class Descafeinado(Bebida):
    """Bebida base: Descafeinado"""
    
    def obtener_descripcion(self) -> str:
        return "Descafeinado"
    
    def obtener_costo(self) -> float:
        return 1.75