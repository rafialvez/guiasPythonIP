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

