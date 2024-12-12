total = 0

print("Programa per calcular la nota mitjana d'un mòdul")

# Demanar el número de notes que s'han d'introduir
notes = int(input("Quantes UF té el mòdul? "))

# Bucle per demanar les notes de cada UF
for i in range(notes):
  notaUF = int(input("Nota de la UF "))
  total += notaUF

# Calcular la mitjana i mostrar el resultat
mitjana = total / notes
print("La nota mitjana d'aquest mòdul és ", mitjana)