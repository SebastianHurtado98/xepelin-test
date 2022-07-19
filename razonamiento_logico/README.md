# Prueba de razonamiento

## Paréntesis balanceado

Para el problema podemos usar un stack que nos ayude a ver si tenemos disponible un paréntesis de apertura para el paréntesis de cierre.
El código asume que solo se trabaja con paréntesis.
Tiene una complejidad algorítmica de O(n)

## Suma 2022

### Binary search

La primera función usa binary search para encontrar el complemento en la lista.
El ordenar la lista nos cuesta O(nlogn) en complejidad de tiempo. Es una solución escalable.

La segunda función usa un hash table (diccionario de python) para encontrar el elemento en O(1). Construir la hash table cuesta O(n).
Esto puede ser más rápido que la función binary search pero a cambio usamos espacio adicional.
