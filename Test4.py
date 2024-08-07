
precio1= int(input("Precio primer polo: "))
precio2= int(input("Precio segundo polo: "))
precio3= int(input("Precio tercer polo: "))

if precio1>precio2>precio3 or precio1>precio3>precio2:
    print("Precio por promoción: " + str(precio2+precio3))

elif precio2>precio1>precio3 or precio2>precio3>precio1:
    print("Precio por promoción: " + str(precio1+precio3))

elif precio3>precio1>precio2 or precio3>precio2>precio1:
    print("Precio por promoción: " + str(precio1+precio2))