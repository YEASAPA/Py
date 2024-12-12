#Defineix les arrays del menú, preus i el total a pagar
menu = []
preus = []
total = 0
z = 0

#Fes que demano 8 plats y preus y que els adereixi a l'array
for i in range(8): 
    nom = input("Com es diu? ")
    preu = float(input("Preu? "))
    menu.append(f"{i+1} - {nom}")
    preus.append(preu)

#Imprimeix el menú amb decoracions
print("MENÚ")
print("----------")

#Això fa que cada element a la array menu es defineixi com a "comida" per que es faci una iteració per cada element a l'array menu.
#Imprimeix cada comida i el preu de cada iteració a la que estem ara.
for comida in menu:
    print(f"{comida}: {preus[z]}€")
    z = z + 1

print("----------")
print("0 - PAGAR")

#Iniciem un bucle infinit
while True:

#Demanem que vols dinar
    print("Què voleu dinar? (Posa 0 per pagar quan hagis acabat)")
    escollir = int(input("Escolleix de la lista (Posant el numeró de plat): "))

#Si es 0 trenques el bucle ja que si ho posem a la condició fa una iteració extra, aquesta es la millor manera
    if escollir == 0:
        break

#Sumem al total el preu
    total += preus[escollir-1]

#Escriu a la terminal quan has de pagar
print(f"Total a pagar: {total}€")
