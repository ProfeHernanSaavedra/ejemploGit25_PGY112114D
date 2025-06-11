def validar_lista_numeros():
    while True:
        listaNumeros = input("Ingrese datos separados por espacio: ").split()
        try:
            numeros = []
            for dato in listaNumeros:
                numeros.append(int(dato))
            return numeros

        except ValueError:
            print("Error, debe ingresar solo numeros enteros!!")

def calculo_pares_impares(numeros):
    pares = []
    impares = []
    for dato in numeros:
        if dato%2 == 0 :
            pares.append(dato)
        else:
            impares.append(dato)
    return pares,impares

lista = (validar_lista_numeros())
pares,impares = calculo_pares_impares(lista)

print("Números pares: ",pares)
print("Números impares: ",impares)

