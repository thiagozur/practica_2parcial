""" Les voy a ser sincero: no entiendo muy bien qué pide este ejercicio. Que redacten mejor.
La suposición es que quiere 30 elementos random ENTRE 0 y 99, y que si alguno de esos es 16
lo diga (y cuántas veces aparece). """

import numpy as np #importamos numpy

vec = np.random.randint(0, 99, size = (1, 30)) #creamos el vector pedido
cant = np.count_nonzero(vec == 16) #contamos todas las ocurrencias del 16 en el vector y las guardamos en cant

print(vec, "\n") #mostramos el vector y una línea vacía
print(f"Hay {cant} vuelo/s para la aerolínea 16.") #mostramos la cantidad de vuelos usando una string con formato