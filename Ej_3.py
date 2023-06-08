""" Les voy a ser sincero: no entiendo muy bien qué pide este ejercicio. Que redacten mejor.
La suposición es que quiere 30 elementos random ENTRE 0 y 99, y que si alguno de esos es 16
lo diga (y cuántas veces aparece). """

import numpy as np

vec = np.random.randint(0, 99, size = (1, 30))
cant = np.count_nonzero(vec == 16)

print(vec, "\n")
print(f"Hay {cant} vuelo/s para la aerolínea 16.")