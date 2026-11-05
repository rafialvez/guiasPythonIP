from queue import LifoQueue as Pila
from queue import Queue as Cola


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