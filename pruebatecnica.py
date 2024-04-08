def ordenar_pares_impares(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    
    resultado = pares + impares
    return resultado

numeros = [50, 20, 9, 82, 58, 77, 1, 23, 14, 22, 2, 55, 33, 48, 64]
resultado = ordenar_pares_impares(numeros)
print("Lista ordenada:", resultado)