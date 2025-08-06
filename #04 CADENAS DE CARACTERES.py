

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

    print(f"Palíndromos: {'Sí' if es_palindromo else 'No'}") # p1[::-1] invierte la palabra → para detectar palíndromos.
    print(f"Anagramas: {'Sí' if es_anagrama else 'No'}") # sorted(p1) ordena las letras → para detectar anagramas.
    print(f"Isogramas: {'Sí' if es_isograma else 'No'}") # len(set(p1)) == len(p1) comprueba que no haya letras repetidas → para detectar isogramas.

analyse_structure_data("amor" , "roma")