# Investigación e Implementación de los Patrones Decorator y Proxy

## Parte 1: Investigación

### Patrón Decorator

**Intención:** El patrón Decorator es un patrón de diseño estructural que permite añadir funcionalidades a objetos colocándolos dentro de objetos envoltorio especiales que contienen estas funcionalidades. Esto permite agregar responsabilidades adicionales a un objeto de manera dinámica sin modificar su estructura.

**Estructura:**

- **Componente:** Define la interfaz para los objetos que pueden tener responsabilidades añadidas.
- **Componente Concreto:** Define un objeto al que se le pueden agregar responsabilidades.
- **Decorador Base:** Mantiene una referencia al componente y define una interfaz conforme a la interfaz del Componente.
- **Decoradores Concretos:** Añaden responsabilidades al componente.

**Ejemplo del mundo real:** Vestir ropa es un ejemplo del uso de decoradores. Cuando tienes frío, te cubres con un suéter. Si sigues teniendo frío a pesar del suéter, puedes ponerte una chaqueta encima. Si está lloviendo, puedes ponerte un impermeable. Todas estas prendas "extienden" tu comportamiento básico pero no son parte de ti, y puedes quitarte fácilmente cualquier prenda cuando lo desees.

### Patrón Proxy

**Intención:** El patrón Proxy es un patrón de diseño estructural que proporciona un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiéndote hacer algo antes o después de que la solicitud llegue al objeto original.

**Estructura:**

- **Interfaz de Servicio:** Define la interfaz común para el Servicio y el Proxy.
- **Servicio:** La clase que proporciona la funcionalidad de negocio útil.
- **Proxy:** Tiene un campo que referencia al servicio. Después de realizar su tarea (control de acceso, cacheo, etc.), pasa la solicitud al servicio.
- **Cliente:** Trabaja con servicios y proxies a través de la misma interfaz.

**Ejemplo del mundo real:** Una tarjeta de crédito es un proxy de una cuenta bancaria, que, a su vez, es un proxy de un manojo de billetes. Ambos implementan la misma interfaz, por lo que pueden utilizarse para realizar un pago. El consumidor se siente genial porque no necesita llevar un montón de efectivo encima. El dueño de la tienda también está contento porque los ingresos de la transacción se añaden electrónicamente a la cuenta bancaria de la tienda sin el riesgo de perder el depósito o sufrir un robo de camino al banco.

### Principal diferencia entre Decorator y Proxy

La principal diferencia radica en su intención:

El **Decorator** está diseñado para añadir funcionalidades a un objeto de forma dinámica y componible. El objeto original no sabe que está siendo decorado, y múltiples decoradores pueden anidarse para combinar comportamientos. El objetivo principal es extender la funcionalidad.

El **Proxy**, por otro lado, controla el acceso al objeto original y actúa como su representante. Aunque el Proxy puede añadir funcionalidad (como cacheo o control de acceso), su propósito principal es gestionar el acceso al objeto real, no necesariamente extender su comportamiento. El Proxy típicamente gestiona todo el ciclo de vida del objeto que representa.

### Escenarios de uso para cada patrón

**Decorator:**

- Cuando necesitas añadir responsabilidades a objetos individuales dinámicamente sin modificar su código
- Cuando la extensión mediante herencia no es práctica o posible
- Cuando necesitas combinar múltiples comportamientos de forma flexible
- Ejemplos: Añadir formateo, compresión o encriptación a flujos de datos; personalizar notificaciones con distintos canales; configurar bebidas con ingredientes adicionales

**Proxy:**

- Inicialización diferida (proxy virtual): Cuando tienes objetos pesados que consumen muchos recursos
- Control de acceso (proxy de protección): Para implementar restricciones basadas en permisos
- Caché de resultados (proxy de caché): Para almacenar resultados de operaciones costosas
- Ejecución remota (proxy remoto): Para acceder a servicios en servidores remotos
- Ejemplos: Control de acceso a bases de datos, carga diferida de imágenes, caché de respuestas de API

## Parte 2: Implementación del Patrón Decorator

He implementado el patrón Decorator en un sistema de café donde podemos añadir dinámicamente ingredientes adicionales (como leche, chocolate, canela) a diferentes tipos de bebidas base.

### Componentes de mi implementación

- **Bebida**: Interfaz abstracta que define el comportamiento base con métodos para obtener descripción y costo
- **Espresso, Americano, Descafeinado**: Implementaciones concretas de Bebida
- **DecoradorBebida**: Clase base para todos los decoradores, mantiene referencia al objeto Bebida
- **Leche, Chocolate, Canela, Crema**: Decoradores concretos que añaden ingredientes y modifican el costo

Esta implementación demuestra perfectamente cómo el patrón Decorator permite:

1. Añadir funcionalidades a objetos existentes sin modificarlos
2. Combinar múltiples decoradores en cualquier orden
3. Mantener el código abierto a extensión pero cerrado a modificación (Principio Open/Closed)
4. Evitar clases con excesivas características mediante composición en lugar de herencia

### Ejecución

Para ejecutar este ejemplo:

```bash
python main.py
```

El resultado mostrará diferentes combinaciones de bebidas con sus ingredientes adicionales y precios calculados dinámicamente.
