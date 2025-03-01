from models.abstract import Ventana

class VentanaWindows(Ventana):
    def __init__(self, titulo):
        self.titulo = titulo
    
    def renderizar(self):
        print(f"Renderizando ventana de Windows con título: {self.titulo}")
    
    def cerrar(self):
        print(f"Cerrando ventana de Windows: {self.titulo}")
    
    # Método exclusivo de Windows
    def maximizar(self):
        print(f"Maximizando ventana de Windows: {self.titulo}")