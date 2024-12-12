#Importa Random
import random

#Fes que la màquina pensi un numero, declarem el nostre marcador de bucle i el marcador d'intents
numero = random.randint(1,100)
i = 0
z = 5

#Fem que si son menys de 5 intents...
while i < 5:

#Et pregunti el numero que ell ha endivinat, informant els intents que queden
    adivina = int(input(f"Adivina el numeró que he pensat, et queden {z} intents: "))

#Si ho endivina et posa Que ho has endivinat en els intents (poso un +1 perquè py comenza desde el 0) i que fagi break
    if adivina == numero:
        print(f"L'has adivinat en {i+1} intents")
        break

#Si no ho has endivinat et diu si es més petit o més gran, suma 1 al numero d'intents fets i baixa 1 als intents restants
    elif adivina > numero:
        print("És més petit")
        i += 1
        z -= 1
    else:
        print("És més gran")
        i += 1
        z -= 1

#Quan es termina el bucle comproba si el número és 5 o no, si ho es et diu que has perdut i quin numero es.
#Si es qualsevol altre numero et diu que has guanyat
if i == 5:
    print(f"Has Perdut. Era {numero}")

else:
    print("Has guanyat!")

