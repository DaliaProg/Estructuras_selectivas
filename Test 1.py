import math
numero = int(input("Digite um numero: "))
cuadrada = int(math.pow(numero, 1/2))
cubica = int(math.pow(numero,1/3))
cuarta = int(math.pow(numero,1/4))

print("Número: " + str(numero))

print("La raíz cuadrada del número: " + str(cuadrada))

print("La raíz cúbica del número: " + str(cubica))

print("La raíz cuarta del número: " + str(cuarta))
