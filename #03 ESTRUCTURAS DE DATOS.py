

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



def es_telefono_valido(telefono):
    return telefono.isdigit() and len(telefono) <= 11


def mostrar_contactos(contactos):
    if not contactos:
        print("La agenda está vacía.")
    else:
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre} - Teléfono: {telefono}")


def agenda_contactos(contactos, accion):
    if accion == "1":  # Buscar
        nombre = input("Nombre del contacto a buscar: ").strip().lower()
        if nombre in contactos:
            print(f"Teléfono de {nombre}: {contactos[nombre]}")
        else:
            print(f"No se encontró el contacto '{nombre}'.")

    elif accion == "2":  # Agregar
        nombre = input("Nombre del nuevo contacto: ").strip().lower()
        if nombre in contactos:
            print("Ese contacto ya existe.")
        else:
            telefono = input("Número de teléfono: ").strip()
            if es_telefono_valido(telefono):
                contactos[nombre] = telefono
                print("Contacto agregado con éxito.")
            else:
                print("Número inválido. Debe ser numérico y de máximo 11 dígitos.")

    elif accion == "3":  # Actualizar
        nombre = input("Nombre del contacto a actualizar: ").strip().lower()
        if nombre in contactos:
            telefono = input("Nuevo número de teléfono: ").strip()
            if es_telefono_valido(telefono):
                contactos[nombre] = telefono
                print("Contacto actualizado correctamente.")
            else:
                print("Número inválido. Debe ser numérico y de máximo 11 dígitos.")
        else:
            print("Ese contacto no existe.")

    elif accion == "4":  # Eliminar
        nombre = input("Nombre del contacto a eliminar: ").strip().lower()
        if nombre in contactos:
            del contactos[nombre]
            print("Contacto eliminado.")
        else:
            print("Ese contacto no existe.")

    elif accion == "5":  # Salir
        print("Saliendo de la agenda...")
        return False

    else:
        print("Opción no válida.")

    return True


def run():
    contactos = {
        "santiago": "3058195931"
    }

    while True:
        print("""\n--- AGENDA DE CONTACTOS ---
1. Buscar un contacto
2. Agregar un contacto
3. Actualizar un contacto
4. Eliminar un contacto
5. Salir
----------------------------""")

        accion = input("Selecciona una opción (1-5): ").strip()
        continuar = agenda_contactos(contactos, accion)
        if not continuar:
            break


if __name__ == '__main__':
    run()







