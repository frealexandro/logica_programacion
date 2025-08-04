# /*
#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */

import random

print("funciones basicas sin parametros\n")

def imprime_numeros_aleatorios():
    print(f"el numero aleatorio es:  {random.random()} \n")

imprime_numeros_aleatorios()




print("funciones basicas sin retorno\n")


def multiplicador_por_10(numero):
    
    print(f"el resultado de la multiplicacion es: {numero**10}\n ")


numero_inicial = 10
print(f"El numero inicial es {numero_inicial}\n")


multiplicador_por_10(numero_inicial) 


print("funciones basicas con parametros\n y con parametros predefinidos") 

def suma(a= 2   , b =16 ):

    #! suma de los valores a + b     
    c = a + b
    
    
    return c


a = 3
b = 5
print(f"los valores a sumar son {a} y {b}\n")

print(f"el resultado de la suma es {suma(a, b)}\n")


print("funciones basicas con parametros determinados\n")

print(f"el resultado de la suma es {suma()}")


print("funciones con varios argumentos\n")

def saludo_con_el_nombre_del_lenguaje(nombre):

    lenguaje = "python"

    return f"hola {nombre}" , f"estas aprendiendo {lenguaje}?"

print(saludo_con_el_nombre_del_lenguaje("santiago"))


print("con un numero variable de argumentos\n")

def saludar(*names):
    for i in names:
        print(i)


saludar("santiago","paula", "el lobo the wall street")

print("con un numero variable de argumentos \n con palabra clave \n")

def datos_pesonales(**datos_personales):
    for key , value in datos_personales.items():
        print(f"este es el valor:  {value}\n de este item: {key} ")


datos_pesonales(
    nombre= "Santiago",
    apellido= "Novoa",
    alias= "mackey",
    age=28

)

print ("Comprueba si puedes crear funciones dentro de funciones.\n")



def funcion_principal_santiago():

    def sub_functon_saludo():
        print("hola como estas mi nombre es santiago\n")


    def sub_function_edad():
        print("mi edad es 23 años\n")

    sub_functon_saludo()
    sub_function_edad()


funcion_principal_santiago()

print("Utiliza algún ejemplo de funciones ya creadas en el lenguaje.(built in functions)\n")


print(len("Santiago\n"))

print(type("MOUREDEV\n"))

print(type(6))

print("santiago\n".upper())

print("SANTIAGO\n".lower())

print("Variables globales y locales\n")


global_var = "santiago".upper()



def saludo():
    local_var = "paula"
    print(f"Hola como estas {local_var}\n")




print(global_var)

#! esta variable solo funcina dentro del scope de la funcion 
#print(local_var)



print("Parte extra para practicar logica\n")

def imprimir_rango(primer_palabra , segunda_palabra):
    
    
    for i in range (0, 100):

        if i % 5 == 0 and i % 3 == 0 :

            print( f"la concatenacion de las palabras es : {primer_palabra} + {segunda_palabra}")


        elif i % 3 == 0 :

            print (f"la primera palabra es {primer_palabra}")

        elif i % 5 == 0 : 

            print(f"la segunda palabra es {segunda_palabra}")

        
        else:
            pass

imprimir_rango("que es lo que es", "dimelo chamo")

