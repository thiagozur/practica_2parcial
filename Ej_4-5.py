import numpy as np
import matplotlib.pyplot as plt

compras = [120, 110, 80, 130, 105 ,85, 85, 85]

compras_vec = np.array(compras)

print("La compra máxima fue de", compras_vec.max(), "mil pesos.")
print("El promedio de precios de las compras es de", compras_vec.mean(), "mil pesos.\n")

plt.plot(compras_vec)

por = input("Ingrese el porcentaje de aumento deseado:\n")

while "%" in por:
    por = por.replace("%", "")

while not por.isnumeric():
    por = input("Porcentaje inadecuado, reintente:\n") 
    por = por.replace("%", "")

por = int(por)
compras_vec_a = compras_vec * (1 + (por/100))
plt.plot(compras_vec_a)
plt.title("Compras de Aeroparque al proveedor de alimentos")
plt.xlabel("Número de compra")
plt.ylabel("Miles de pesos")
plt.legend(["Compras", f"Aumento del {por}%"])
plt.show()
