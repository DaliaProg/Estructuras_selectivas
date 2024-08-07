
compra= int(input("Ingrese el monto total de su compra: "))

if compra>=250:
    descuento=round((12/100)*compra,2)
    print("¡Felicitaciones! Obtuvo un descuento de: S/." + str(descuento))
    print("Monto final a pagar: " + str(compra-descuento))

else:
    print("Monto final a pagar: S/." + str(compra))
