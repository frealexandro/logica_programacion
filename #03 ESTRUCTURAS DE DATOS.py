

# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
#  *   en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización
#  *   y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más
#  *   de 11 dígitos (o el número de dígitos que quieras).
#  * - También se debe proponer una operación de finalización del programa.
#  */



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




#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización
#  *   y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más
#  *   de 11 dígitos (o el número de dígitos que quieras).
#  * - También se debe proponer una operación de finalización del programa.
#  */




print(" \n DIFICULTAD EXTRA (opcional): \n")



