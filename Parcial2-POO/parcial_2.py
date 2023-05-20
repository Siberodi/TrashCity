#  Por: Sibeli Isaeth Rodríguez Díaz
#  C.E.200058702

from abc import ABC, abstractmethod


#Esta clase es una implementación de un patrón Singleton. 
# Permite crear una única instancia de TrashCity.
class TrashCity:
    _instance = None 

    def __new__(cls, ID):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, ID):
        self.ID = ID

    def mostrarListaResiduos(self):
        print("Clasificación de Residuos")
        print("1. Vidrio  2. Papel")

#Esta clase es una clase abstracta que define la interfaz para los diferentes estados de una ruta.
class EstadoRuta(ABC):
    @abstractmethod
    def tonResiduos(self, ruta):
        pass

    @abstractmethod
    def finalizar_ruta(self, ruta):
        pass


#Esta clase define el estado de una ruta activa.
class EstadoRutaActiva(EstadoRuta):
    def tonResiduos(self,ruta, TrashCity): #agrega toneladas de residuos a una ruta activa. Permite al usuario seleccionar el tipo de residuo (vidrio o papel) y especificar la cantidad recolectada en cada localización geográfica.
        TrashCity.mostrarListaResiduos()
        sw = 1
        while sw == 1:
            print("--------------------------------------------------------------")
            op = int(input("Seleccione el tipo de residuo a añadir -->"))
            if op == 1:
                for i in range(len(ruta.geo)):
                    cantidad = float(input(f"¿Cuanto vidrio recogió en esta localización?  {ruta.geo[i]} --->  "))
                    ruta.TONvidrio.append(cantidad)
            elif op == 2:
                for i in range(len(ruta.geo)):
                    cant = float(input(f"¿Cuanto papel recogió en esta localización?  {ruta.geo[i]}  ---> "))
                    ruta.TONpapel.append(cant)
            sw = int(input("¿Desea añadir otro residuo?  1.Si  2.No -->  "))
        
        print()
        print("Se añadió la cantidad correctamente")
        print()

    #finaliza una ruta activa. Permite al usuario ingresar el tiempo transcurrido y la carga total de residuos recolectados en la ruta.    
    def finalizar_ruta(self, ruta):
        tiempo = str(input("¿Cuánto tiempo pasó hasta finalizar el recorrido? --> "))
        ruta.tiempoRecorrido = tiempo
        carga = float(input("¿Cuántas TON de residuos recogió en total? --->  "))
        ruta.cargaCamion = carga
        print()
        print("Se ha finalizado la ruta en un tiempo de " + ruta.tiempoRecorrido)
        print()
        # Cambiar el estado de la ruta al estado finalizado
        ruta.set_estado(EstadoRutaFinalizada())


#Esta clase define el estado de una ruta finalizada.
class EstadoRutaFinalizada(EstadoRuta):
    def tonResiduos(self, ruta):
        print("No se pueden añadir más residuos a una ruta finalizada.")

    def finalizar_ruta(self, ruta):
        print("La ruta ya ha sido finalizada.")

#Esta clase representa una ruta de recogida de residuos.
class ruta:
    def __init__(self, Puntolatitud = str, Puntolongitud= str, dia = str ):
      self.Puntolatitud = Puntolatitud   #latitud de la localización de la ruta
      self.Puntolongitud = Puntolongitud #longitud de la localización de la ruta.
      self.cargaCamion = float           #carga total de residuos recolectados en la ruta.
      self.dia = dia                     #día de la ruta.
      self.TONvidrio = []                #lista de toneladas de vidrio recolectadas en cada localización geográfica.
      self.TONpapel = []                 #lista de toneladas de papel recolectadas en cada localización geográfica.
      self.geo = []                      #lista que almacena la latitud y longitud de cada localización geográfica.
      self.local_geografica(Puntolatitud, Puntolongitud)
      self.tiempoRecorrido = str         #tiempo transcurrido en la ruta.
      self.estado = EstadoRutaActiva()   #objeto que representa el estado actual de la ruta.

    def local_geografica(self, Puntolatitud, Puntolongitud):
        localizacion = []
        self.geo.append(Puntolatitud)
        self.geo.append(Puntolongitud)

    def set_estado(self, estado): #establece el estado de la ruta al estado proporcionado.
        self.estado = estado

    def tonResiduos(self, TrashCity: TrashCity): #Delega la responsabiidad de agregar toneladas de residuos a la ruta al estado actual
        self.estado.tonResiduos(self, TrashCity)

    def finalizar_ruta(self):
        self.estado.finalizar_ruta(self)


#Esta clase representa un camión utilizado para la recogida de residuos.
class Camion:
    def __init__(self):
        self.placa = str
        self.conductor_ID = int
        self.conductor_name = str
        self.asis1_name = str
        self.asis2_name = str
        self.asis1_ID = int
        self.asis2_ID = int

#solicita al usuario ingresar los detalles del camión, como la placa, el nombre del conductor y los nombres e IDs de los asistentes.
    def agregarListado(self):
        print("")
        print("--------------------------------------------------------------")
        placa = str(input(f"Placa del vehículo -->  "))
        self.placa = placa
        conductor_name = str(input(f"Nombre del Conductor --> "))
        self.conductor_name = conductor_name
        conductor_ID = int(input(f"ID conductor --> "))
        self.conductor_ID = conductor_ID
        asis1_name = str(input(f"Nombre del Asistente 1 --> "))
        self.asis1_name = asis1_name
        asis1_ID = int(input(f"ID del Asistente 1 --> "))
        self.asis1_ID = asis1_ID
        asis2_name = str(input(f"Nombre del Asistente 2 --> "))
        self.asis2_name = asis2_name
        asis2_ID = int(input(f"ID del Asistente 2 --> "))
        self.asis2_ID = asis2_ID
        print("--------------------------------------------------------------")
        print("")

#Esta clase representa un turno de trabajo en una ruta de recogida de residuos.
class turno:
    def __init__(self, ruta: ruta):
        self.tiempo_recorrido = ruta.tiempoRecorrido

    #calcula y devuelve la cantidad total de toneladas de vidrio recolectadas en la ruta.
    def calcularTonVidrio(self, ruta):
        TonVidrio = sum(ruta.TONvidrio)
        print("--------------------------------------------------------------")
        print("Las toneladas totales de vidrio recogidas son: ")
        return TonVidrio
    
    #calcula y devuelve la cantidad total de toneladas de papel recolectadas en la ruta.
    def calcularTonPapel(self, ruta):
        TonPapel = sum(ruta.TONpapel)
        print("--------------------------------------------------------------")
        print("Las toneladas totales de papel recogidas son: ")
        return TonPapel
  

#Implementación
trashcity = TrashCity(17630000)
camion1 = Camion()
camion1.agregarListado()


Ruta1 = ruta("10o 29' ", "73o 15'", "19/03")
Ruta1.tonResiduos(trashcity)
Ruta1.finalizar_ruta()

TurnoAM = turno(Ruta1)
TurnoAM.calcularTonVidrio(Ruta1)