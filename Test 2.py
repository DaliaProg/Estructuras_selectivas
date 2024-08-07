
numero1= int(input("Write the first number: "))
numero2= int(input("Write the second number: "))
numero3= int(input("Write the third number: "))

if numero1>numero2>numero3:
    print("Suma: " + str(numero1+numero3))
    print("Resta: " + str(numero1-numero3))
    print("Multiplicación: " + str(numero1*numero3))

elif numero1>numero3>numero2:
    print("Suma: " + str(numero1+numero2))
    print("Resta: " + str(numero1-numero2))
    print("Multiplicación: " + str(numero1*numero2))

elif numero2>numero3>numero1:
    print("Suma: " + str(numero2+numero1))
    print("Resta: " + str(numero2-numero1))
    print("Multiplicación: " + str(numero2*numero1))

elif numero2 > numero1 > numero3:
        print("Suma: " + str(numero2+numero3))
        print("Resta: " + str(numero2-numero3))
        print("Multiplicación: " + str(numero2*numero3))

elif numero3>numero2>numero1:
    print("Suma: " + str(numero3+numero1))
    print("Resta: " + str(numero3-numero1))
    print("Multiplicación: " + str(numero3*numero1))


elif numero3>numero1>numero2:
    print("Suma: " + str(numero3+numero2))
    print("Resta: " + str(numero3-numero2))
    print("Multiplicación: " + str(numero3*numero2))