"""
Enunciado:

Crea una función llamada 'count_fruits(fruits_list)' que reciba como parámetro una lista
de frutas y retorne un diccionario donde cada llave sea el nombre de una
fruta y su valor sea la cantidad de veces que aparece en la lista.

Parámetros:
    fruits_list: lista de frutas

Retorno:
    Un diccionario donde cada llave es el nombre de una fruta y su valor es
    la cantidad de veces que aparece en la lista.

Ejemplo:
    Entrada:
    fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
    count_fruits(fruits)

    Salida:
    {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}
"""


def count_fruits(fruits_list):
    fruit_count = {}
    for fruit in fruits_list:
        if fruit in fruit_count:
            fruit_count[fruit] += 1 #la clave es actualizar el valor de conteo en cada iteracion
        else:
            fruit_count[fruit] = 1
    return fruit_count

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script

fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
print(count_fruits(fruits))