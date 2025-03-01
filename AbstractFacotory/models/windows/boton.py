from models.abstract import Boton

class BotonWindows(Boton):
    def __init__(self, texto):
        self.texto = texto
    
    def renderizar(self):
        print(f"Renderizando botón de Windows con texto: {self.texto}")
    
    def onClick(self):
        print(f"Click en botón de Windows: {self.texto}")
        
    # Método exclusivo de Windows
    def aplicar_tema_windows(self):
        print(f"Aplicando tema Windows 11 al botón: {self.texto}")