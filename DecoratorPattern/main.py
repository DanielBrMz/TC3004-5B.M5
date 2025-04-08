from bebidas import Espresso, Americano, Descafeinado
from decoradores import Leche, Chocolate, Canela, Crema

def mostrar_bebida(bebida):
    """Muestra la descripción y costo de una bebida"""
    print(f"Pedido: {bebida.obtener_descripcion()}")
    print(f"Precio: ${bebida.obtener_costo():.2f}\n")

def main():
    # Ejemplo 1: Espresso con Leche y Canela
    mi_bebida = Espresso()
    mi_bebida = Leche(mi_bebida)
    mi_bebida = Canela(mi_bebida)
    mostrar_bebida(mi_bebida)
    
    # Ejemplo 2: Americano con Chocolate
    mi_bebida2 = Americano()
    mi_bebida2 = Chocolate(mi_bebida2)
    mostrar_bebida(mi_bebida2)
    
    # Ejemplo 3: Descafeinado con Leche, Chocolate y Crema
    mi_bebida3 = Descafeinado()
    mi_bebida3 = Leche(mi_bebida3)
    mi_bebida3 = Chocolate(mi_bebida3)
    mi_bebida3 = Crema(mi_bebida3)
    mostrar_bebida(mi_bebida3)

if __name__ == "__main__":
    main()