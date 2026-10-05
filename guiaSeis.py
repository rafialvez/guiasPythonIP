import math

def imprimir_hola_mundo():
    return print("¡Hola mundo!")

raizDe2 = round(math.sqrt(2),4) 

factorial_2 = math.factorial(2)

perimetro = 2*math.pi

#ejercicio 2

def imprimir_saludo(saludo: str) ->str:
    return print("Hola",saludo)

def raiz_cuadrada_de(numero: int) ->float:
    return math.sqrt(numero)

def fahrenheit_a_celsius(temp_far: float) -> float:
    res = ((temp_far - 32)* (5/9))
    return res

def imprimir_dos_veces(estribillo: str) -> str:
    return print(estribillo*2)

def es_multiplo_de(n:int, m:int) ->bool:
    if (n%m) == 0:
        return True
    else:
        return False

def es_par(numero:int) -> bool:
    return es_multiplo_de(numero,2)

#ejercicio 3
def alguno_es_0(numero1:int, numero2:int)->bool:
    return (numero1==0 or numero2==0)

def ambos_son_0(numero1:int, numero2:int)->bool:
    return (numero1==0 and numero2==0)

def es_nombre_largo(nombre:str)->bool:
    return (len(nombre)>=3) and (len(nombre)<=8)

def es_bisiesto(año:int)->bool:
    return (((año%400)==0) or (año%4==0 and not(año%100==0)))

def peso_pino(metros:float)->float:
    if metros<=3:
        peso = (metros*100)*3
    else:
        peso = 3*100*3 + (metros-3)*100*2
    return peso

def es_peso_util(peso:float)->bool:
    return peso>=400 and peso<=1000

def sirve_pino(altura_pino:float)->bool:
    return es_peso_util(peso_pino(altura_pino))