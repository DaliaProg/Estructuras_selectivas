
patos=int(input("¿Cuántos patos hay?: "))

gallinas=int(input("¿Cuántos gallinas hay?: "))

cerdos=int(input("¿Cuántos cerdos hay?: "))

conejos=int(input("¿Cuántos conejos hay?: "))

total=(patos+gallinas+cerdos+conejos)

ppatos=int((patos/total)*100)

pgallinas=int((gallinas/total)*100)

pcerdos=int((cerdos/total)*100)

pconejos=int((conejos/total)*100)

print("En total hay "+ str(total) + " animales")
print("Porcentaje de patos: " + str(ppatos) + "%")
print("Porcentaje de gallinas: " + str(pgallinas) + "%")
print("Porcentaje de cerdos: " + str(pcerdos) + "%")
print("Porcentaje de conejos: " + str(pconejos) + "%")