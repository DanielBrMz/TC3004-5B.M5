from factories.windows_factory import WindowsFactory
from factories.mac_factory import MacFactory

# Cliente que usa la fábrica
def crear_ui(factory):
    boton = factory.crear_boton("Aceptar")
    ventana = factory.crear_ventana("Aplicación Demo")
    
    # Usamos los productos
    ventana.renderizar()
    boton.renderizar()
    boton.onClick()
    ventana.cerrar()
    
    # Demostración de métodos exclusivos
    if isinstance(factory, WindowsFactory):
        factory.crear_tema_oscuro()
        from models.windows.boton import BotonWindows
        from models.windows.ventana import VentanaWindows
        if isinstance(boton, BotonWindows):
            boton.aplicar_tema_windows()
        if isinstance(ventana, VentanaWindows):
            ventana.maximizar()
    
    elif isinstance(factory, MacFactory):
        factory.aplicar_transparencia()
        from models.mac.boton import BotonMac
        from models.mac.ventana import VentanaMac
        if isinstance(boton, BotonMac):
            boton.aplicar_efecto_hover()
        if isinstance(ventana, VentanaMac):
            ventana.mostrar_traffic_lights()

if __name__ == "__main__":
    # Configuración para Windows
    print("=== Creando UI para Windows ===")
    windows_factory = WindowsFactory()
    crear_ui(windows_factory)
    
    print("\n=== Creando UI para Mac ===")
    mac_factory = MacFactory()
    crear_ui(mac_factory)