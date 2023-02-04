#Elias García

### --> Punto 1 <-- ###
def verificarDiagonales(matriz):
    diagonalIzq, diagonalDer, valor = 0, -1, True
    while diagonalIzq < len(matriz) and valor == True:
        if matriz[diagonalDer][diagonalIzq] != matriz[diagonalDer][diagonalDer]:
            valor = False
        diagonalIzq  += 1
        diagonalDer -= 1
    return valor


### --> Punto 2 <-- ###
def esCapicua(lista):
    mitad = len(lista) // 2
    i, j = 0, -1
    valor = True
    while i < mitad and valor == True:
        if lista[i] != lista[j]: valor = False
        i += 1
        j -= 1
    return valor

### --> Punto 3a <-- ###
def verificarRepetidos(listaRepetidos, numeroRepetido):
    valor = False
    if numeroRepetido in listaRepetidos:
        valor = True
    else:
        listaRepetidos.append(numeroRepetido)
    return valor

def diferenciaListas(listaA, listaB):
    listaNoRepetidos = []
    listaRepetidos = []
    i = 0
    while i < len(listaA):
        valor = True
        j = 0
        while j < len(listaB) and valor == True:
            if listaA[i] == listaB[j]:
                if verificarRepetidos(listaRepetidos, [listaB[j], j]) == False:
                    valor = False
            j += 1
        if valor == True:
            listaNoRepetidos.append(listaA[i])
        i += 1
    return listaNoRepetidos

### --> Punto 3b <-- ###
def leerListas():
    i = 0
    cantidadEjecuciones = int(input())
    while i < cantidadEjecuciones:
        listaA = input().split()
        listaA = listaA[1::]
        for j in range(len(listaA)):
            listaA[j] = int(listaA[j])
        listaB = input().split()
        listaB = listaB[1::]
        for j in range(len(listaB)):
            listaB[j] = int(listaB[j])
        print(diferenciaListas(listaA, listaB))
        i += 1

### --> Punto 4 <-- ###
def sumatoriaCifras(numero):
    i = numero // 10
    j =( i % 10) + (numero % 10)
    while i >= 10:
        i /= 10
        i += i % 10
    return j

def verificarPrimo(numero):
    for i in range(2,int(numero/2) + 1):
        if (numero%i) == 0:
            return False
    return True

def mostrarPrimos(numero):
    i = 3
    anteriorPrimo = 2
    listaSumaCifras = [anteriorPrimo]
    print("Numeros primos entre el 1 y %d:" %numero)
    while i <= numero:
        if verificarPrimo(i) == True:
            print("--> %d," %anteriorPrimo)
            anteriorPrimo = i
            numeroSumaCifra = sumatoriaCifras(i)
            if verificarPrimo(numeroSumaCifra) == True:
                listaSumaCifras.append(i)
        i += 1
    print("--> %d\n" %anteriorPrimo)
    print("Números entre 1 y %d con suma de dígitos con valor primo:" %numero)
    for j in range (len(listaSumaCifras) - 1):
        print("%d" %listaSumaCifras[j], end = ", ")
    print(listaSumaCifras[-1])


### --> Punto 5 <-- ###

def sumaValoresMatriz(matrizD, listaPos):
    sumatoriaMatriz, i = 0, 0
    while i < len(listaPos):
        if listaPos[i][0] in mat:
            j, valor = 0, True
            while valor == True and j < len(matrizD[listaPos[i][0]]):
                if matrizD[par[i][0]][j][0] == listaPos[i][1]:
                    sumatoriaMatriz += matrizD[listaPos[i][0]][j][1]
                    valor = False
                j += 1
        i += 1
    return sumatoriaMatriz

