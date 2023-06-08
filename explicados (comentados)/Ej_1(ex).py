scan = input("Ingrese código de vuelo o 'finalizar' para terminar:\n") #tomamos el número de vuelo
vuelos = [] #creamos una lista vacía para ir guardando los vuelos ingresados
vuelos_dict = {
    "L": [],
    "C": [],
    "I": [],
} #creamos un diccionario vacío que vamos a usar para guardar los vuelos organizados según tipo

while scan != "finalizar": #repetimos este proceso hasta que el usuario escriba finalizar
    if len(scan) != 5: #comprobamos que la cantidad de caracteres del código sea la correcta
        scan = input("Cantidad de caracteres incorrecta. Reintente o ingrese 'finalizar':\n")
    else:
        if scan[:-1].isnumeric() and (scan[-1:] == "L" or scan[-1:] == "C" or scan[-1:] == "I"):
            #comprobamos que haya cuatro números y una de las tres letras correctas y, de ser así,
            #agregamos el vuelo a la lista y volvemos a preguntar por otro
            vuelos.append(str(scan))
            scan = input("Ingrese código de vuelo o 'finalizar' para terminar:\n")
        else:
            #si los datos están mal, se pide reingresarlos
            scan = input("Números o tipo de vuelo inadecuados. Reintente o ingrese 'finalizar':\n")

for v in vuelos: #repetimos esto para cada vuelo v de la lista vuelos
    ciudad = v[:2] #tomamos los primeros dos números de v para la ciudad
    aerolinea = v[2:4] #tomamos los segundos dos números de v para la aerolínea
    tipo = v[4:] #tomamos el último caracter de v para el tipo de vuelo
    vuelos_dict[tipo].append((ciudad, aerolinea))
    #guardamos en el diccionario una tupla con la ciudad y la aerolinea en la clave (key)
    #que hayamos guardado en la variable llamada tipo (que solo puede ser C, L o I porque ya lo comprobamos antes)

cant_L = 0 #iniciamos la cantidad de vuelos locales en 0
for i in vuelos_dict["L"]:
    cant_L += 1 #por cada vuelo i guardado en la clave L del diccionario, sumamos uno a la cantidad de vuelos locales

print(f"Hay {cant_L} vuelos locales.\n")
#mostramos la cantidad de vuelos locales usando una string con formato (con variables dentro)

cant_v = 0 #iniciamos la cantidad de vuelos de las ciudades 74 y 18 en 0

for i in vuelos_dict: #repetimos esto para cada clave i del diccionario
    if vuelos_dict[i] != []:
        #esto solo lo hacemos si lo que está guardado en la clave i no es una lista vacía para evitar erorres
        for n in vuelos_dict[i]: #repetimos esto para cada tupla n guardada en la lista de la clave i
            if n[0] == "74": 
                cant_v +=1 #sumamos uno a la cantidad si el primer valor de la tupla (la ciudad) es 74
            elif n[0] == "18":
                cant_v += 1 #sumamos uno a la cantidad si el primer valor de la tupla (la ciudad) es 18

print(f"Hay {cant_v} vuelos a las ciudades 74 o 18.\n")
#mostramos la cantidad de vuelos a las ciudades 74 o 18 usando una string con formato