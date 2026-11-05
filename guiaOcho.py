from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

#ejercicio 1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int)->Pila[int]:
    pilaConNros: Pila[int] = Pila()
    for i in range(cantidad):
        pilaConNros.put(random.randint(desde,hasta))
    return pilaConNros

def cantidad_elementos(p: Pila)->int:
    i: int = 0
    pilaTemporal: Pila = Pila()
    while not p.empty():
        valor_de_pila = p.get()
        pilaTemporal.put(valor_de_pila)
        i += 1
    while not pilaTemporal.empty():
        p.put(pilaTemporal.get())
    return i

def buscar_el_maximo(p: Pila[int])->int:
    pilaTemporal: Pila = Pila()
    max: int = p.get()
    p.put(max)
    while not p.empty():
        valor_temp: int = p.get()
        if valor_temp>max:
            max = valor_temp
        pilaTemporal.put(valor_temp)
    while not pilaTemporal.empty():
        p.put(pilaTemporal.get())
    return max

def buscar_nota_maxima(p: Pila[(str,int)])->tuple[str,int]:
    pilaTemporal: Pila = Pila()
    referencia: tuple[str,int] = p.get()
    nota_referencia: int = referencia[1]
    p.put(referencia)
    while not p.empty():
        valor_temp: int = p.get()
        nota = valor_temp[1]
        if nota>nota_referencia:
            nota_referencia = nota
            referencia = valor_temp
        pilaTemporal.put(valor_temp)
    while not pilaTemporal.empty():
        p.put(pilaTemporal.get())
    return nota_referencia

#colas

def generar_colas_al_azar(cantidad:int, desde:int, hasta: int)->Cola[int]:
    cola: Cola[int] = Cola()
    for i in range(cantidad):
        cola.put(random.randint(desde,hasta))
    return cola

def problema_cantidad_elementos(c:Cola)->int:
    cant: int = 0
    colaTemporal: Cola = Cola()
    while not c.empty():
        valor = c.get()
        colaTemporal.put(valor)
        cant +=1
    while not colaTemporal.empty():
        c.put(colaTemporal.get())
    return cant

def buscar_el_maximo_cola(c: Cola[int])->int:
    lista_de_cola: list[int] = []
    while not c.empty():
        valor: int = c.get()
        lista_de_cola.append(valor)
    max = lista_de_cola[0]
    for i in lista_de_cola:
        if i>max:
            max = i
        c.put(i)
    return max

def buscar_nota_minima(c: Cola[tuple[str,int]])->tuple[str,int]:
    lista_de_cola: list[int] = []
    while not c.empty():
        valor: int = c.get()
        lista_de_cola.append(valor)
    nota_referencia: tuple[str,int] = lista_de_cola[0]
    min: int = lista_de_cola[0][1]
    for (nombre, nota) in lista_de_cola:
        if nota<min:
            min = nota
            nota_referencia = (nombre,nota)
        c.put((nombre,nota))
    return nota_referencia

def calcular_promedio_por_estudiante(notas:list[(str,float)])->dict[str,float]:
    dict_notas: dict[str,float] = {}
    lista_estudiantes: list[str] = []
    lista_notas: list[list[float]] = []
    promedios_notas: list[float] = []
    for notas_con_estudiante in notas:
        nombre: str = notas_con_estudiante[0]
        if nombre not in lista_estudiantes:
            lista_estudiantes.append(nombre)
    for nombre in lista_estudiantes:
        for notas_con_estudiante in notas:
            notas_temporales: list[float] = []
            nombre_de_notas : str = notas_con_estudiante[0]
            nota : float = notas_con_estudiante[1]
            if nombre_de_notas==nombre:
                notas_temporales.append(nota)
            lista_notas.append(notas_temporales)
    if len(lista_estudiantes)!=len(lista_notas):
        return False
    for i in range(len(lista_estudiantes)):
        nombre = lista_estudiantes[i]
        notas_de_nombre = lista_notas[i]
        dict_notas[nombre].append(promedio(notas_de_nombre))
    return dict_notas

def calcular_promedio_por_clase(notas:list[tuple[str,float]])->dict[str,float]:
    res_con_notas: dict[str,list[float]] = {}
    
    for (nombre, calificacion) in notas:
        if nombre not in res_con_notas.keys():
            res_con_notas[nombre] = [calificacion]
        else:
            res_con_notas[nombre].append(calificacion)
    
    dic_con_promedio: dict[str,float] = {}
    nombres_con_notas = res_con_notas.items()
    for (nombre,lista_notas) in nombres_con_notas:
        dic_con_promedio[nombre] = promedio(lista_notas)
    return dic_con_promedio

#ejercicio 17
#historiales = dict[usuarios,pilasDeStrings]
def problema_visitar_sitio(historiales: dict[str,Pila[str]],usuario:str,sitio:str):
    usuario_encontrado: bool = False
    usuarios = historiales.keys()
    for usuario_en_historiales in usuarios:
        if usuario_en_historiales == usuario:
            usuario_encontrado = True
            pilaDelUsuario: Pila = historiales[usuario]
            pilaDelUsuario.put(sitio)
            historiales[usuario] = pilaDelUsuario
    if usuario_encontrado == False:
        sitios:Pila = Pila()
        sitios.put(sitio)
        historiales[usuario] = sitios

def problema_navegar_atras(historiales: dict[str,Pila[str]],usuario:str)->str:
    usuarios: list[str] = historiales.keys()
    for usuario_de_historiales in usuarios:
        if usuario==usuario_de_historiales:
            pilaDelUsuario: Pila = historiales[usuario]
            ultimoSitio = pilaDelUsuario.get()
            historiales[usuario] = pilaDelUsuario
    return ultimoSitio

def agregar_producto(inventario: dict[str, dict[str, int|float]], nombre: str, precio: float, cantidad: int)-> None:
    dic_de_nombre: dict[str,float] = {"precio": precio, "cantidad": cantidad}
    inventario[nombre] = dic_de_nombre

def actualizar_stock(inventario: dict[str, dict[str, int|float]], nombre: str, cantidad: int)-> None:
    dic_con_nueva_cant : dict[str, int|float] = inventario[nombre]
    dic_con_nueva_cant["cantidad"] = cantidad
    inventario[nombre] = dic_con_nueva_cant

def actualizar_precio(inventario: dict[str, dict[str, int|float]], nombre: str, precio: float)-> None:
    dic_con_nueva_cant : dict[str, int|float] = inventario[nombre]
    dic_con_nueva_cant["precio"] = precio
    inventario[nombre] = dic_con_nueva_cant
    
def calcular_valor_inventario(inventario: dict [str, dict[str, int|float]])->float:
    valor_total: float = 0
    productos: list[str] = inventario.keys()
    for producto in productos:
        precio_prod: int|float = inventario[producto]["precio"]
        cant_prod: int = inventario[producto]["cantidad"]
        valor_prod: float = precio_prod*cant_prod
        valor_total += valor_prod
    return valor_total

def promedio(lista_notas: list[float])->float:
    return sumatoria(lista_notas)/len(lista_notas)

def sumatoria(lista: list[float])->float:
    res: float = 0
    for i in lista:
        res += i
    return res

inventario = {"remera":{"precio":1000,"cantidad":10}}
print(calcular_valor_inventario(inventario))