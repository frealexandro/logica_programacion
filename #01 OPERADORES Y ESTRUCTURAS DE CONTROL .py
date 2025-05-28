# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

#all: operadores aritmeticos

#! variables

a = 5 
b = 6

#! suma
print(a + b )

#! resta
print (a - b)

#! multiplicacion 
print (a * b )

#! elevacion
print(a**b)

#! modulo
print(a % b)

#!division
print(a / b)

#! division entera
print(a//b)


#all: operadores de comparacion

#! igualdad
print( a == b )

#! desigualdad
print(a != b)

#! mayor que , mayor o igual que
print(a > b) 
print(a >= b)

#! menor que
print(a < b)
print( a <= b)

#all: operadores de comparacion

#! and
print (a < b and 3 < 6 )

#! or 
print (a < b or 7 < 6 )

#! nor
print (not a > b )


#all : operadores de asignacion

#! asignacion
animal =  'gato'
print(animal)

#! suma y asignacion
animal += animal
print(animal)


#! multiplicacion y asignacion 
numero = 2
numero *= 2
print(numero)

#! resta y asignacion 
numero -= 2
print(numero)

#! elevacion y asignacion
numero **= 5
print(numero)
#! division y asignacion
numero /= 23
print(numero)

#! dvision entera y asignacion 
numero //= 23
print(numero)

#all: operadores de identidad 
my_new_number = numero

#! esta en la misma ubicacon en memoria
print(my_new_number is numero)

#! no esta en la misma ubicacion en memoria
print(my_new_number is not numero)

#all: operadores de pertenecia

#! esta en 
print('o' in 'santiago')

#! no esta en 
print('o' not in 'santiago')


#all: operaciones con bit
a = 3 # 0011
b = 10 # 1010

#! operador and 
print(a & b)  # 0010

#! operador or 
print(a | b) # 1011

#!operador xor 
print(a ^ b) # 1001

#! operador not
print(~ a) 

#! desplazamiento a la derecha 
print(a >> b)

#! desplazamiento a la izquierda 
print(a << b)




#all: estructuras de control condicionales


#! condicional if and elif , else
my_string = "Santiago"

if my_string == "Santiago":

    print("my string is Santiago")

elif my_string == "Novoa":

    print("my string is Novoa")

else:
    print("no tengo ningun string")

#all: estructuras de control iterativas

#! estructura iterativa for 
for i in range (11):
    print(i)


#! condicional while 
i = 0

while i <= 10 :
    print(i)
    i+=1

#all: estructuras de control con excepciones 

try:
    print(10 / 0 )
except:
    print("se a producido un error")
finally:
    print("ha finalizado el manejo de excepciones \n")







#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.


print("dificultad extra")

def dificultad_extra(): 

    for i in range (10 , 55):
    
        
        
        if i % 3 == 0 :
            continue

        elif i % 2 == 0 :
            continue


        elif i == 16 : 
    
            continue
    
        else:
        
            print(i) 


dificultad_extra()
