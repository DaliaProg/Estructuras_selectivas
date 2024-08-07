
numeros= input("Ingrese doce números enteros separados por comas: ")
suma=0
for i in numeros:
    if numeros!=",":
        suma=suma+int(i)
        print(suma)
