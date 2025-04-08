from bebidas import Bebida

class DecoradorBebida(Bebida):
    """Clase base para todos los decoradores"""
    
    def __init__(self, bebida: Bebida):
        self._bebida = bebida
    
    def obtener_descripcion(self) -> str:
        return self._bebida.obtener_descripcion()
    
    def obtener_costo(self) -> float:
        return self._bebida.obtener_costo()


class Leche(DecoradorBebida):
    """Decorador que añade leche a la bebida"""
    
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()} + Leche"
    
    def obtener_costo(self) -> float:
        return self._bebida.obtener_costo() + 0.50


class Chocolate(DecoradorBebida):
    """Decorador que añade chocolate a la bebida"""
    
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()} + Chocolate"
    
    def obtener_costo(self) -> float:
        return self._bebida.obtener_costo() + 0.75


class Canela(DecoradorBebida):
    """Decorador que añade canela a la bebida"""
    
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()} + Canela"
    
    def obtener_costo(self) -> float:
        return self._bebida.obtener_costo() + 0.25


class Crema(DecoradorBebida):
    """Decorador que añade crema a la bebida"""
    
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()} + Crema"
    
    def obtener_costo(self) -> float:
        return self._bebida.obtener_costo() + 0.60