import math

# Entrada
num = float(input("Ingrese un número real: "))

# Cálculos
raiz = math.sqrt(abs(num))
cuadrado = num ** 2
cubo = num ** 3
absoluto = abs(num)
entero = int(num)
redondeado = round(num)
seno = math.sin(num)
coseno = math.cos(num)
tangente = math.tan(num)

# Salida
print(f"\nResultados para el número {num}:")
print(f"Raíz cuadrada: {raiz}")
print(f"Cuadrado: {cuadrado}")
print(f"Cubo: {cubo}")
print(f"Valor absoluto: {absoluto}")
print(f"Parte entera: {entero}")
print(f"Redondeado: {redondeado}")
print(f"Seno: {seno}")
print(f"Coseno: {coseno}")
print(f"Tangente: {tangente}")


