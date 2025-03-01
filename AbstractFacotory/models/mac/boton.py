from models.abstract import Boton

class BotonMac(Boton):
    def __init__(self, texto):
        self.texto = texto
    
    def renderizar(self):
        print(f"Renderizando botón de Mac con texto: {self.texto}")
    
    def onClick(self):
        print(f"Click en botón de Mac: {self.texto}")
    
    # Método exclusivo de Mac
    def aplicar_efecto_hover(self):
        print(f"Aplicando efecto hover elegante al botón Mac: {self.texto}")