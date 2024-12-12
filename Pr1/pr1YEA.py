#Fet per Yussef El Alami SMX2C, con copyright valido hasta el 15/09/2025 para que ya no me puedan quitar la nota si se le doy el codigo a un amigo
#(no voy a darselo a nadie, es broma)
#Demanar el DNI, preu, descompte i IVA
DNI = int(input("Escriu el teu DNI: "))
Preu = int(input("Ingresa el preu del article: "))
Descompte = float(input("Ingresa el descompte: "))
IVA = float(input("Ingresa l'IVA: "))

#Calculem el DNI
NIF = DNI % 23
Ni = "TRWAGMYFPDXBNJZSQVHLCKE"
Nifull = Ni[NIF]

#Calculem el preu final
SacarPorcentaje = Descompte / 100
SacarIVA = IVA / 100
DescF = Preu - Preu * SacarPorcentaje
PreuF = DescF + DescF * SacarIVA

#Imprimim el DNI y el Preu final
print(f"EL teu NIF és: {DNI}{Nifull}")
print(f"EL teu preu final és: {PreuF}")