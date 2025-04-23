def mayor_suma_consecutivos(lista):
    if len(lista) < 2:
        return None
    max_suma = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > max_suma:
            max_suma = suma
    return max_suma
print(mayor_suma_consecutivos([1, 5, 3, 2]))

#explicacion: se debe calcular la suma de cada uno de los elementos consecutivos y se debe guardar la mayor cantidad de la suma
