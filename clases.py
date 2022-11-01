#EJERCICIO CALCULADORA
#Formular una calculadora utilizando clases. 
#utilizar buenas prácticas como anotaciones y excepciones'
"""class Calculadora:
    numero:int = 0
    numero2:int = 0
    def suma(self,num:int,num2: int)-> int:
        numero = num
        numero2 = num2
        
        return numero + numero2
       

mi_suma = Calculadora()

try:
    n1:int = int(input("Ingresa el primero numero: "))
    n2:int = int(input("Ingresa el segundo  numero: "))

    result = mi_suma.suma(n1,n2)
    print(result)
except Exception as ex:
    print("*********\n Error por favor ingrese solo numeros\n********\n ",ex)"""



"""Cree una clase figura, que tenga los siguientes atributos.
Nombre
Área
Coordenada X
Coordenada Y
Escriba sus respectivos getters y setters de área.

Y cree el método mostrar_figura, qué imprima lo siguiente:

La figura se llama "Nombre"
Tiene un área de "Área" m^2
E inicia en las coordenadas ( "X", "Y" )
Luego, cree un objeto con los siguiente datos.

Nombre = Círculo
Área = 30.5
Coordenada X = -1
Coordenada Y = 2
Llame al método mostrar_figura, y luego destruya el objeto."""

class Figura:
    def __init__(self,nombre: str, area:float ,x:int , y:int, zeta:int) -> None:
        self.__nombre = nombre
        self.__area = area
        self.__x = x    #modo privado
        self.y = y   #esta en modo publico
        self.__z = zeta  #no se va modificar

    def __del__(self):
        return None

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def get_coor_x(self):
        return self.__x
    
    def set_coor_x(self,x):
        self.__x = x


    def mostrarFigura(self):
        print("****************")
        print(f"La figura se llama {self.__nombre}")
        print(f"Tiene un area de {self.get_area()} m^2")
        print(f"He inicia en las coordenadas ({self.__x},{self.y})")
        print(f"El valor de z: {self.__z}")

figura = Figura("Circulo",30.5,-1,2,5)
figura.set_area(50.5)
figura.__x = 10

figura.y = 8
figura.mostrarFigura()

figura.set_coor_x(100)
figura.get_coor_x()
figura.__z = 53  # z no se modifico
figura.mostrarFigura()
#del figura


#EJERCIO -------------
"""Cree una clase Automovil con los siguientes atributos.

Marca
Año
Placa
Número de Asientos
Escriba los getters y setter del atributo marca.

Cree dos métodos, mostrar_carro y tipo_carro.

mostrar_carro imprime:

El carro es de marca "Marca" del año "Año"
Y tiene placa número "Placa"
tipo_carro imprime:

Si el número de asientos es mayor a 20, imprimir:

El automóvil es un bus.
Si el número de asientos es mayor a 10, imprimir:

El automóvil es una combi.
Si no, imprimir:

El automóvil es un carro normal
Crear un objeto con los siguientes datos, y 
llamar a los métodos creados.

Marca = Suzuki
Año = 2010
Placa = ABC-456
Número de Asientos = 4
'''
"""


"""class Automovil:
    def __init__(self,marca:str ,anio: int,placa: str,nro_asientos:int) -> None:
        self.__marca = marca
        self.__anio = anio
        self.__placa = placa
        self.__nro_asientos = nro_asientos
    
    def __del__(self):
        return None

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def mostrar_carro(self):
        print(f"El carro es de marca {self.__marca} del año {self.__anio} ")
        print(f"Nro de asientos: {self.__nro_asientos}")
        print(f"Y tiene placa numero {self.__placa}")

    def tipo_carro(self):
        if self.__nro_asientos >= 20:
            print("El automóvil es un bus.")
        elif self.__nro_asientos >= 10:
            print("El automóvil es una combi.")
        else:
            print("El automóvil es un carro normal")

automovil = Automovil("Suzuki",2010,"ABC-456",22)
print("------------- Metodo mostrar carro -------")
automovil.mostrar_carro()
print("------------- Metodo tipo carro ----------")
automovil.set_marca("Honda")
automovil.tipo_carro()
del automovil
"""

"""Cree una clase Punto con los siguientes atributos: X, Y

Cree el método mostrar_punto, el cual imprime lo siguiente.

El punto está en ( "X", "Y" )
Luego realice la composición con la clase figura creada anteriormente.

Nota:
Utilice el método mostrar_punto dentro de mostrar_figura
Utilice los mismos datos del ejercicio anterior
Cree un objeto Figura y llame a mostrar_figura,
 luego elimine el objeto."""

"""class Punto:
    def __init__(self):
        #self.__x = x
        #self.__y = y
        self.figura1 = Figura("Cuadrado",2,15,20,5)
        

    def __del__(self):
        return None

    def mostrar_punto(self):
        print(f"El punto esta en {self.__x}, {self.__y}")


a = Punto()
a.mostrar_punto()"""