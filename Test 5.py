import math
hipotenusa = int(input("Ingrese la hipotenusa: "))

cateto1 = int(input("Ingrese el primer cateto: "))

cateto2 = int(math.pow((hipotenusa**2 - cateto1**2), 1/2))

print("El segundo cateto es: " + str(cateto2))