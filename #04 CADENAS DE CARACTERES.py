

"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""




print ( " \n Operaciones  \n")

#! Concatenacion 

s1 = "Hola"

s2 = "Mundo"


print( s1 + ", " + s2 + "!" )

#! Repeticion

print(s1 * 3)

#! Indexacion 

print(s1[0])

#! longitud 

print(len(s2))

#! slicing

print(s2[2:6])

print(s2[:2])

#! busqueda 

print ("a" in s1) 
print ("i" in s1) 

#! remplazo

print(s1.replace("a","o"))


#! division 

print(s2.split("n"))


#! mayusculas y minusculas

print(s1.upper())
print(s1.lower())

print("santiago novoa".title())
print("santiago novoa".capitalize())

#! eliminacion espacios delante y atras

print("santiago novoa ".strip())

#! busqueda al principio y al final 

print(s1.startswith("Ho"))
print(s1.endswith("la"))

#! busqueda de posicion 

print("santiago Novoa".find("ti"))
print("santiago Novoa".lower().find("no"))

#! busqueda de ocurrencias

print("santiago Novoa".lower().count("a"))


#! formatear una cadena

s1 = "Hola"
s2 = "Python"
s3 = "Santiago Novoa Rojas"

print("Saludo: {}, Lenguaje: {}".format(s1,s2))

#! Interpolacion

print(f"Saludo: {s1}, Lenguaje: {s2}")

#! Transformacion de cadena de caracteres a lista

print(list(s3))

l1 = [s1, ", ", s2, "!"]
print("".join(l1))  

#! Transformaciones Numericas
s4 = "1234"
s4 = int(s4)
print(s4)


s5 = "12345.6"
s5 = float(s5)
print(s5)


s4 = "1234"
#! comprobaciones varias 
print(s4.isalpha())
print(s4.isalnum())





# print(" \n DIFICULTAD EXTRA (opcional): \n")
# #  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
# #  * para descubrir si son:
# #  * - Palíndromos
# #  * - Anagramas
# #  * - Isogramas    


# def analyse_structure_data (p1 , p2):

#     p1 = p1.lower()
#     p2 = p2.lower()
    
#     es_palindromo = p1 == p1[::-1] and p2 == p2[::-1]
#     es_anagrama = sorted(p1) == sorted(p2)
#     es_isograma = len(set(p1)) == len(p1) and len(set(p2)) == len(p2)

#     print(f"Palíndromos: {'Sí' if es_palindromo else 'No'}") # p1[::-1] invierte la palabra → para detectar palíndromos.
#     print(f"Anagramas: {'Sí' if es_anagrama else 'No'}") # sorted(p1) ordena las letras → para detectar anagramas.
#     print(f"Isogramas: {'Sí' if es_isograma else 'No'}") # len(set(p1)) == len(p1) comprueba que no haya letras repetidas → para detectar isogramas.

# analyse_structure_data("amor" , "roma")