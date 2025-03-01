from models.abstract import UIFactory
from models.mac.boton import BotonMac
from models.mac.ventana import VentanaMac

class MacFactory(UIFactory):
    def crear_boton(self, texto="OK"):
        return BotonMac(texto)
    
    def crear_ventana(self, titulo="Ventana de Mac"):
        return VentanaMac(titulo)
    
    # Método exclusivo de MacFactory
    def aplicar_transparencia(self):
        print("Aplicando efectos de transparencia en componentes Mac")