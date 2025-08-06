

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



#! list
#* is a estructure simple mutable

print( "\n Estructure of data : List \n" )

my_list = ["black" , "santiago", "paula" ]


print(my_list)

my_list.append("julian") #dd

print(my_list)

my_list.remove("black") #delete

print(my_list)

my_list[1] = "cuervillo" #update element

print(my_list)

my_list.sort() #sort

print (my_list)

#! tuples
#* is inmutable

print( "\n Estructure of data : tuple \n")

my_tuple = ("santiago" , "jhoner300@gmail.com" , "23" )

print(my_tuple[0]) #access

my_tuple = tuple(sorted(my_tuple))

print(my_tuple)

print(type(my_tuple)) 

#! sets 
#* there are not duplicates
#* there are not positons  

print ( "\n Estructure of data : set \n" ) 

my_set = {"santiago" , "jhoner300@gmail.com" , "23"}
print(my_set)


my_set.add("@santiagonov")

my_set.add("@santiagonov")


my_set.remove("santiago")

#my_set = sorted(my_set)

#print(my_set[0])

print(my_set)

print(type(my_set))

#! diccionarys
#* keys #hashing


print("\n Estructure of data : dictccionary \n")


my_dict: dict = {"name":"santiago" , "email":"jhoner300@gmail.com" , "age":"23"}  


print(my_dict["age"]) #acess

my_dict["age"] = "24" # update
print(my_dict)

#del my_dict["age"] #delete
#print(my_dict)

my_dict = dict(sorted(my_dict.items())) # sort
print(my_dict)

print(type(my_dict))


print(" \n DIFICULTAD EXTRA (opcional): \n")
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas    


def analyse_structure_data (p1 , p2):

    p1 = p1.lower()
    p2 = p2.lower()
    
    es_palindromo = p1 == p1[::-1] and p2 == p2[::-1]
    es_anagrama = sorted(p1) == sorted(p2)
    es_isograma = len(set(p1)) == len(p1) and len(set(p2)) == len(p2)

    print(f"Palíndromos: {'Sí' if es_palindromo else 'No'}")
    print(f"Anagramas: {'Sí' if es_anagrama else 'No'}")
    print(f"Isogramas: {'Sí' if es_isograma else 'No'}")

analyse_structure_data("amor" , "roma")
