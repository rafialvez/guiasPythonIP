#ejercicio 1
def pertenece(s:list[int], e:int)->bool:
    res:bool = False
    for i in s:
        res = res or e == i
    return res

#para tateti

def pertenece_str(s:list[str], e:str)->bool:
    res:bool = False
    for i in s:
        res = res or e == i
    return res

def suma_total(s: list[int])->int:
    res = 0
    for i in range(0,len(s)):
        res = res + s[i]
    return res

def divide_a_todos(s:list[int],e:int)->bool:
    divide:bool = True
    for i in s:
        if i%e!=0:
            divide = False
    return divide

def maximo(s:list[int])->int:
    max =s[0]
    for i in s:
        if i>=max:
            max = i
    return max

def minimo(s:list[int])->int:
    min =s[0]
    for i in s:
        if i<=min:
            min = i
    return min

def ordenados(s:list[int])->bool:
    i=0
    estaOrdenado:bool = True
    while estaOrdenado == True and i<len(s)-1:
        if s[i]>=s[i+1]:
            estaOrdenado = False
        i += 1
    return estaOrdenado

def pos_maximo(s:list[int])->int:
    if s==[]:
        res:int=-1
    else:
        res:int=0
        for i in range(0,len(s)):
            if s[i]>s[res]:
                res = i
    return res

def pos_minimo(s:list[int])->int:
    if s==[]:
        res:int=-1
    else:
        res:int=0
        for i in range(0,len(s)):
            if s[i]<=s[res]:
                res=i
    return res

def long_mayorASiete(s:list[str])->bool:
    hayMayores:bool = False
    for palabra in s:
        if len(palabra)>7:
            hayMayores = True
    return hayMayores

def es_palindroma(s:str)->bool:
    laPalabraEsPalindroma:bool = False
    if len(s)<=1:
        laPalabraEsPalindroma = True
    else:
        inversoPalabra:str = da_vuelta_str(s)
        if inversoPalabra == s:
            laPalabraEsPalindroma = True
    return laPalabraEsPalindroma
#este ejercicio va dentro del 2
def da_vuelta_str(s:str)->str:
    palabra_nueva:str = ""
    for i in s:
        palabra_nueva= i + palabra_nueva 
    return palabra_nueva
#
def iguales_consecutivos(s:list[int])->bool:
    hayTresIguales = False
    k = 0
    j = k + 1
    i = k + 2
    while hayTresIguales == False and i<len(s):
        if s[k]==s[j] and s[j]==s[i]:
            hayTresIguales = True
        k +=1 
        j +=1
        i +=1
    return hayTresIguales

#ejercicio 2
def cerosEnPosicionesPares(s:list[int])->list[int]:
    for i in range (0,len(s)):
        if i%2==0:
            s[i]=0

def cerosEnPosicionesPares2(s:list[int])->list[int]:
    listaNueva:list[int] = []
    for i in range(0,len(s)):
        if i%2==0:
            listaNueva.append(0)
        else:
            listaNueva.append(s[i])
    return listaNueva

def sin_vocales(s:str)->str:
    palabraSinVocales:str = ""
    for i in s:
        if es_vocal(i)==False:
            palabraSinVocales = palabraSinVocales + i
    return palabraSinVocales

def es_vocal(letra:str)->bool:
    es_vocal = False
    for i in ["a","e","i","o","u"]:
            es_vocal = es_vocal or letra == i
    return es_vocal

def reemplaza_vocales(s:str)->str:
    palabraSinVocales:str = ""
    for i in s:
        if es_vocal(i)==True:
            palabraSinVocales = palabraSinVocales + "_"
        else:
            palabraSinVocales = palabraSinVocales + i
    return palabraSinVocales
#revisar!!
def eliminar_repetidos(s:str)->str:
    palabra_sin_repetidos = ""
    for i in s:
        palabra_sin_repetidos += i
        s = quitar_repetidos(s,i)
    return palabra_sin_repetidos

def quitar_repetidos(palabra:str,letra:str)->str:
    palabraSinRepetidos:str = ""
    for i in palabra:
        if i!=letra:
            palabraSinRepetidos = palabraSinRepetidos + i
    return palabraSinRepetidos

def resultadoMateria(notas:list[int])->int:
    todasNotas4=True
    res:int = 3
    for i in notas:
        if i<4:
            todasNotas4 = False
    if todasNotas4==True:
        if (suma_total(notas)/len(notas))>=7:
            res = 1
        else:
            res = 2
    return res

def saldoActual(movimientos:list[(str,int)])->int:
    saldoInicial:int=0
    for (tipo,cantidad) in movimientos:
        if tipo=="I":
            saldoInicial += cantidad
        elif tipo=="R":
            saldoInicial -= cantidad
    return saldoInicial

def es_matriz(s:list[list[int]])->bool:
    res:bool = False
    if len(s)>0 and len(s[0])>0:
        if longitudIgual(s)==True:
            res = True
    return res

def longitudIgual(s:list[list[int]])->bool:
    sonTodasIguales = True
    longitudParametro = len(s[0])
    for i in s:
        if len(i)!=longitudParametro:
            sonTodasIguales = False
    return sonTodasIguales

#ejercicio 3: matrices
def pertenece_a_cada_uno_version_1(s:list[list[int]],e:int)->list[bool]:
    perteneceEnCadaUno:list[bool] = []
    for fila in s:
        perteneceEnCadaUno.append(pertenece(fila,e))
    return perteneceEnCadaUno

type tipoMatriz = list[list[int]]

def filas_ordenadas(m:tipoMatriz)->list[bool]:
    lista_booleanos_filas:list[bool] = []
    for fila in m:
        lista_booleanos_filas.append(ordenados(fila))
    return lista_booleanos_filas

def columna(m:tipoMatriz, c:list[int])->list[int]:
    lista_columna:list[int] = []
    for fila in m:
        lista_columna.append(fila[c])
    return lista_columna

def columnas_ordenadas(m:tipoMatriz)->list[bool]:
    matriz_de_columnas:tipoMatriz = transponer(m)
    return filas_ordenadas(matriz_de_columnas)

def transponer(m:list[list[int]])->list[list[int]]:
    columnas: list[list[int]] = []
    cant_filas = len(m)
    cant_columnas = len(m[0])
    for i in range(cant_columnas):
        columna:list[int] = []
        for j in range(cant_filas):
            columna.append(m[j][i])
        columnas.append(columna)
    return columnas

def quien_gana_tateti(m:list[list[str]])->int:
    res:int = 2
    if casos_O_ganadora(m) == True:
        res = 0
    elif casos_X_ganadora(m) == True:
        res = 1
    return res

def casos_O_ganadora(m:list[list[str]])->bool:
    res = False
    for fila in m:
        if pertenece_str(fila,"X")==False:
            res = True
    for falsaFila in transponer(m):
        if pertenece_str(falsaFila,"X")==False:
            res = True
    diagonal:list[str] = funcion_diagonal(m)
    if pertenece_str(diagonal,"X")==False:
        res = True
    return res

def casos_X_ganadora(m:list[list[str]])->bool:
    res = False
    for fila in m:
        if pertenece_str(fila,"O")==False:
            res = True
    for falsaFila in transponer(m):
        if pertenece_str(falsaFila,"O")==False:
            res = True
    diagonal:list[str] = funcion_diagonal(m)
    if pertenece_str(diagonal,"O")==False:
        res = True
    return res

def funcion_diagonal(m:list[list[str]])->list[str]:
    diagonal:list[str] = []
    cant_filas = len(m)
    cant_columnas = cant_filas
    i:int=0
    j:int=0
    while i < cant_filas:
        while j<cant_columnas:
            if i==j:
                diagonal.append(m[i][j])
            j = j + 1
        j = 0
        i = i+1
    return diagonal

def lista_de_estudiantes():
    lista: list[str] = []
    estudiante: str = input("Introducí el nombre del capo de tu estudiante")
    while estudiante != "listo":
        lista.append(estudiante)
        estudiante
    return lista