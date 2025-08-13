


# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */


#! tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_a = 30

print(my_int_a)
print(my_int_b)


#! tipos de dato por referencia 


my_list_a = [10 , 20]
my_list_b = my_list_a

my_list_b.append(30)

print(my_list_a)
print(my_list_b)

#! funciones de datos por valor 

my_int_c = 10 

def my_int_func(my_int:int):
    my_int = 20
    print(my_int)


my_int_func(my_int_c)
print(my_int_c)

#! funiones de datos por referencia 

my_list_c = [20 , 30]


def my_list_func(my_list:list):
    my_list.append(20)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_func(my_list_c)
print(my_list_c)




#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

variable_valor_1 = 15
variable_valor_2 = 20

print(f"El valor de la variable 1 es: {variable_valor_1} y el valor de la variable 2 es: {variable_valor_2}")

def funcion_por_valor(variable_valor_1 : int , variable_valor_2: int ):
    
    variable_valor_1_2 = variable_valor_2

    variable_valor_2_1 = variable_valor_1

    return variable_valor_1_2 , variable_valor_2_1
    
    

variable_valor_1 , variable_valor_2 = funcion_por_valor(variable_valor_1 , variable_valor_2)

print(f"El valor nuevo de la variable 1 es: {variable_valor_1} y el valor nuevo de la variable 2 es: {variable_valor_2}")









def funcion_por_referencia(variable_1 : list , variable_2: list ):
    pass
