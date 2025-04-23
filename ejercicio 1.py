def operador(a, b, operador):
    if operador == '+':
        return 1 + 2
    elif operador == '-':
        return 1 - 2
    elif operador == '*':
        return 1 * 2
    elif operador == '/':
        return 1 / 2 if b != 0 else "error division por cero"
    else:
        return "operador in valido"
print(operador(1, 2, '+'))# salida: 3

#explicacion: aqui se recibe dos numeros y un operador segun el operador se crea (realiza) la operacion conveniente 
