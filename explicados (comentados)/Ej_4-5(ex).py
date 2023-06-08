import numpy as np #importamos numpy
import matplotlib.pyplot as plt #importamos matplotlib.pyplot

compras = [120, 110, 80, 130, 105 ,85, 85, 85] #definimos la lista de las compras

compras_vec = np.array(compras) #convertimos la lista en un vector de numpy

print(f"La compra máxima fue de {compras_vec.max()} mil pesos.")
#mostramos el valor máximo usando una string con formato
print(f"El promedio de precios de las compras es de {compras_vec.mean()} mil pesos.\n")
#mostramos el valor promedio usando una string con formato

plt.plot(compras_vec) #colocamos el vector en el gráfico

por = input("Ingrese el porcentaje de aumento deseado:\n") #guardamos la entrada de porcentaje

while "%" in por:
    por = por.replace("%", "") #quitamos todos los % que haya escrito la persona hasta que no quede ninguno

while not por.isnumeric(): #repetimos esto solo mientras lo que nos queda luego de quitar los % no sea un número
    por = input("Porcentaje inadecuado, reintente:\n") #volvemos a pedir el porcentaje
    por = por.replace("%", "") #quitamos los % de nuevo luego de cada intento

por = int(por) #convertimos la string ingresada en un número entero
compras_vec_a = compras_vec * (1 + (por/100))
#le sumamos el porcentaje pedido a los valores del vector y lo guardamos en otra variable
plt.plot(compras_vec_a) #agregamos este otro vector al gráfico
plt.title("Compras de Aeroparque al proveedor de alimentos") #título del gráfico
plt.xlabel("Número de compra") #etiqueta del eje x
plt.ylabel("Miles de pesos") #etiqueta del eje y
plt.legend(["Compras", f"Aumento del {por}%"]) #nombres para cada vector graficado, se colocan en el orden previo
plt.show() #mostramos el gráfico
