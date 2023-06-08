scan = input("Ingrese código de vuelo o 'finalizar' para terminar:\n")
vuelos = []
vuelos_dict = {
    "L": [],
    "C": [],
    "I": [],
}

while scan != "finalizar":
    if len(scan) != 5:
        scan = input("Cantidad de caracteres incorrecta. Reintente o ingrese 'finalizar':\n")
    else:
        if scan[:-1].isnumeric() and (scan[-1:] == "L" or scan[-1:] == "C" or scan[-1:] == "I"):
            vuelos.append(str(scan))
            scan = input("Ingrese código de vuelo o 'finalizar' para terminar:\n")
        else:
            scan = input("Números o tipo de vuelo inadecuados. Reintente o ingrese 'finalizar':\n")

for v in vuelos:
    ciudad = v[:2]
    aerolinea = v[2:4]
    tipo = v[4:]
    vuelos_dict[tipo].append((ciudad, aerolinea))

cant_L = 0
for i in vuelos_dict["L"]:
    cant_L += 1

print(f"Hay {cant_L} vuelos locales.\n")

cant_v = 0

for i in vuelos_dict:
    if vuelos_dict[i] != []:
        for n in vuelos_dict[i]:
            if n[0] == "74":
                cant_v +=1
            elif n[0] == "18":
                cant_v += 1

print(f"Hay {cant_v} vuelos a las ciudades 74 o 18.\n")