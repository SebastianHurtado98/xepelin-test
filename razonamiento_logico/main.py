"""
Paréntesis balanceado:
Para el problema podemos usar un stack que nos ayude a ver si tenemos
disponible un paréntesis de apertura para el paréntesis de cierre.

El código asume que solo se trabaja con paréntesis.
"""

def balanced(cadena):
    stack = []
    for c in cadena:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack or stack.pop() != "(":
                 return False
    return not stack

cadena = "(())))"
print(balanced(cadena))
cadena = "()()()"
print(balanced(cadena))
cadena = ")))"
print(balanced(cadena))


"""
Suma 2022
La primera función usa binary search para encontrar el complemento en la lista.
El ordenar la lista nos cuesta O(n*logn) en complejidad de tiempo. Es una solución escalable.

La segunda función usa un hash table (diccionario de python) para encontrar el elemento
en O(1). Construir la hash table cuesta O(n). Esto puede ser más rápido que la función
binary search pero a cambio usamos espacio adicional.
"""


lista_de_prueba_a = [10, 2012, 1, 2, 3, 4, 5, 1]
lista_de_prueba_b = [10, 10, 20, 30]

def find(lista, y):
    left = 0
    right = len(lista) - 1
    mid = 0
    while left <= right:
        mid = (right + left) // 2
        if lista[mid] < y:
            left = mid + 1
        elif lista[mid] > y:
            right = mid - 1
        else:
            return True
    return False

def suma_2022_bs(lista):
    lista.sort()
    for x in lista:
        y = 2022 - x
        if find(lista, y):
            return True
    return False



def suma_2022_ht(lista):
    ht = dict()
    for x in lista:
        ht[x] = True
    for x in lista:
        y = 2022 - x
        if y in ht:
            return True
    return False


print(suma_2022_bs(lista_de_prueba_a))
print(suma_2022_bs(lista_de_prueba_b))

print(suma_2022_ht(lista_de_prueba_a))
print(suma_2022_ht(lista_de_prueba_b))