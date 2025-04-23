def mismos_caracteres(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def filtrar_programas(lista):
    resultado = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if mismos_caracteres(lista[i], lista[j]):
                if lista[i] not in resultado:
                    resultado.append(lista[i])
                if lista[j]not in resultado:
                    resultado.append(lista[j])
    return resultado
 print(filtrar_programas(["amor", "roma", "perro"])) # salida ['amor', 'roma']
