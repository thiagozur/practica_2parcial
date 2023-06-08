d_vuelos = {
    "1474": "L",
    "2520": "C",
    "1625": "C",
    "1725": "L",
}

def buscar_vuelo(vuelos, tipo):
    coincidencias = ""
    cant = 0
    for v in vuelos:
        if vuelos[v] == tipo:
            coincidencias += (v + ", ")
            cant += 1
    text = f"Hay {cant} vuelos del tipo {tipo}: {coincidencias[:-2]}."
    return text

print(buscar_vuelo(d_vuelos, "C"))