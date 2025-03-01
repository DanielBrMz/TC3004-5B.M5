from models.abstract import UIFactory
from models.windows.boton import BotonWindows
from models.windows.ventana import VentanaWindows

class WindowsFactory(UIFactory):
    def crear_boton(self, texto="OK"):
        return BotonWindows(texto)
    
    def crear_ventana(self, titulo="Ventana de Windows"):
        return VentanaWindows(titulo)
    
    # Método exclusivo de WindowsFactory
    def crear_tema_oscuro(self):
        print("Activando tema oscuro para todos los componentes Windows")