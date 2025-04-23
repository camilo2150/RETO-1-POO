def es_palindromo(palabra):
    n = len(palabra)
    for i in range(n // 2):
        if palabra[i] != palabra[n - 1 - i]:
            return i
    return n
print(es_palindromo("n")) # salida: n
print(es_palindromo("i")) # salida: i

#explicacion: se compara cadaaracter desde su inicio con cada parte desde su final, si usar slicing
