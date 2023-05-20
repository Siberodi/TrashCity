# TrashCity
Solución al enunciado del parcial 2 de programación orientada a objetos, sobre un programa de manejo de datos de la empresa de manejo de residuos "Trash City"

# Manual de Usuario - Código de Recolección de Residuos TrashCity

Este manual proporciona una descripción y guía de uso para el código de Trash City. El código consiste en una serie de clases y métodos que permiten gestionar rutas de recolección, registrar la cantidad de residuos recogidos y calcular estadísticas relacionadas.

## Requisitos del sistema
- Python 3.x instalado en el sistema.

## Instalación
1. Descarga el archivo que contiene el código de recolección de residuos.
2. Descomprime el archivo en la ubicación deseada.

## Uso del programa
1. Abre un terminal o línea de comandos.
2. Navega hasta la ubicación donde se encuentra el archivo del código.
3. Ejecuta el siguiente comando para ejecutar el programa:

```shell
python parcial_2.py
```

## Descripción del código

El código está compuesto por varias clases que interactúan entre sí para gestionar las rutas de recolección de residuos. A continuación, se describen las principales clases y métodos utilizados:

### Clase TrashCity

Esta clase implementa el patrón Singleton, lo que significa que solo se puede crear una instancia de la clase. Se utiliza para representar la ciudad encargada de la recolección de residuos.

Métodos:
- `mostrarListaResiduos()`: Muestra una lista de los tipos de residuos disponibles para clasificar.

### Clase EstadoRuta (Clase abstracta)

Esta clase define una interfaz para los diferentes estados de una ruta. Es una clase abstracta que debe ser implementada por las clases concretas.

Métodos:
- `tonResiduos(ruta)`: Método abstracto para agregar toneladas de residuos a una ruta.
- `finalizar_ruta(ruta)`: Método abstracto para finalizar una ruta.

### Clase EstadoRutaActiva

Esta clase define el estado de una ruta activa, donde se pueden agregar toneladas de residuos y finalizar la ruta.

Métodos:
- `tonResiduos(ruta, TrashCity)`: Permite al usuario seleccionar el tipo de residuo (vidrio o papel) y especificar la cantidad recolectada en cada localización geográfica.
- `finalizar_ruta(ruta)`: Permite al usuario ingresar el tiempo transcurrido y la carga total de residuos recolectados en la ruta.

### Clase EstadoRutaFinalizada

Esta clase define el estado de una ruta finalizada, donde no se pueden agregar más residuos ni finalizar la ruta.

Métodos:
- `tonResiduos(ruta)`: Muestra un mensaje indicando que no se pueden agregar más residuos a una ruta finalizada.
- `finalizar_ruta(ruta)`: Muestra un mensaje indicando que la ruta ya ha sido finalizada.

### Clase ruta

Esta clase representa una ruta de recogida de residuos y contiene los datos relacionados con la ruta y los residuos recogidos.

Atributos:
- `Puntolatitud`: Latitud de la localización de la ruta.
- `Puntolongitud`: Longitud de la localización de la ruta.
- `cargaCamion`: Carga total de residuos recolectados en la ruta.
- `dia`: Día de la ruta.
- `TONvidrio`: Lista de toneladas de vidrio recolectadas en cada localización geográfica.
- `TONpapel`: Lista de toneladas de papel en cada localización geográfica.
- `geo`: Lista que almacena la latitud y longitud de cada localización geográfica.
- `tiempoRecorrido`: Tiempo transcurrido en la ruta.
- `estado`: Objeto que representa el estado actual de la ruta.

Métodos:
- `local_geografica(Puntolatitud, Puntolongitud)`: Agrega la latitud y longitud proporcionadas a la lista `geo`.
- `set_estado(estado)`: Establece el estado de la ruta al estado proporcionado.
- `tonResiduos(TrashCity)`: Delega la responsabilidad de agregar toneladas de residuos a la ruta al estado actual de la ruta.
- `finalizar_ruta()`: Delega la responsabilidad de finalizar la ruta al estado actual de la ruta.

### Clase Camion

Esta clase representa un camión utilizado para la recogida de residuos.

Atributos:
- `placa`: Placa del vehículo.
- `conductor_ID`: ID del conductor del camión.
- `conductor_name`: Nombre del conductor del camión.
- `asis1_name`: Nombre del asistente 1 del camión.
- `asis2_name`: Nombre del asistente 2 del camión.
- `asis1_ID`: ID del asistente 1 del camión.
- `asis2_ID`: ID del asistente 2 del camión.

Métodos:
- `agregarListado()`: Solicita al usuario ingresar los detalles del camión, como la placa, el nombre del conductor y los nombres e IDs de los asistentes.

### Clase turno

Esta clase representa un turno de trabajo en una ruta de recogida de residuos.

Atributos:
- `tiempo_recorrido`: Tiempo de recorrido de la ruta.

Métodos:
- `calcularTonVidrio(ruta)`: Calcula y devuelve la cantidad total de toneladas de vidrio recolectadas en la ruta.
- `calcularTonPapel(ruta)`: Calcula y devuelve la cantidad total de toneladas de papel recolectadas en la ruta.

## Flujo de trabajo típico

El flujo de trabajo típico para utilizar el código de recolección de residuos sería el siguiente:

1. Crear una instancia de la clase `TrashCity` para representar la ciudad de recolección.
2. Crear una instancia de la clase `ruta` para representar una ruta de recogida de residuos.
3. Agregar los detalles del camión utilizando la clase `Camion`.
4. Agregar las toneladas de residuos en cada localización geográfica utilizando el método `tonResiduos` de la clase `ruta`.
5. Finalizar la ruta utilizando el método `finalizar_ruta` de la clase `ruta`.
6. Calcular las estadísticas de la ruta utilizando la clase `turno`.

Recuerda que puedes personalizar el código y agregar más funcionalidades según tus necesidades.

## Contribuciones

Si deseas contribuir a este proyecto, puedes enviar tus sugerencias o mejoras a través de un pull request en GitHub.

## Soporte

Si necesitas ayuda o tienes alguna pregunta, puedes contactar al equipo de soporte en support@trashCity.com.

¡Gracias por utilizar nuestro sistema de recolección de residuos! Esperamos que sea de utilidad en tu labor de mantener nuestra ciudad limpia y saludable.
Somos, Trash City, tu empresa de recolección de residuos favorita.
