d_vuelos = {
    "1474": "L",
    "2520": "C",
    "1625": "C",
    "1725": "L",
} #creamos el diccionario pedido

def buscar_vuelo(vuelos, tipo): #definimos la función pedida con los parámetros vuelos y tipo
    coincidencias = "" #creamos una string vacía para guardar los vuelos que coinciden
    cant = 0 #creamos una variable con la cantidad de vuelos coincidentes comenzada en 0
    for v in vuelos: #repetimos esto para cada clave v del diccionario que pondremos en el parámetro vuelos
        if vuelos[v] == tipo:
            #hacemos esto solo si lo que hay guardado en la clave v es igual a la string que pusimos en el parámetro tipo
            coincidencias += (v + ", ")
            #agregamos a la string coincidencias el número de vuelo v, una coma y un espacio
            cant += 1 #sumamos uno a la cantidad
    text = f"Hay {cant} vuelos del tipo {tipo}: {coincidencias[:-2]}." #guardamos los vuelos en una string con formato
    return text #devolvemos la variable text

print(buscar_vuelo(d_vuelos, "C"))
#print de prueba llamando a la función usando el diccionario d_vuelos como parámetro vuelos y
#a la string "C" como paráemtro tipo. La función devuelve una string que luego es mostrada con print()