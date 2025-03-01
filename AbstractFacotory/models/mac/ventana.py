from models.abstract import Ventana

class VentanaMac(Ventana):
    def __init__(self, titulo):
        self.titulo = titulo
    
    def renderizar(self):
        print(f"Renderizando ventana de Mac con título: {self.titulo}")
    
    def cerrar(self):
        print(f"Cerrando ventana de Mac: {self.titulo}")
    
    # Método exclusivo de Mac
    def mostrar_traffic_lights(self):
        print(f"Mostrando controles traffic light en ventana Mac: {self.titulo}")