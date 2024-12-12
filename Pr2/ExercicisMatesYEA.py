#Importa el paquet random.
import random

#Defineix el rang del 2 numeros aleatoris i la llista de operadors on un d'aquests sera agafat aleatoriament.
numero1 = random.randint(0,10)
numero2 = random.randint(0,10)
operadorlist = "+-/%*"
operador = random.choice(operadorlist)

#Iniciem la funció.
def exercici():

#Primer li enseñem al usuari l'operació.
    print(f"{numero1}{operador}{numero2}")

#I internament la resolvem abans de que pregunti quin es el resultat.
#Ja que s'executa en el mateix fil no pasa res si posem diferents linees, sempre serà el mateix numero.
    resultat = int(eval(f"{numero1}{operador}{numero2}"))

#Li demanem el resultat al usuari.
    operacio = int(input("Digues el resultat:"))

#Si la operació es correcta et diu que molt be i t'ensenya el resultat.
#Si no et diu que esta malament i t'ensenya el resultat igualment.
    if resultat == operacio:
        print(f"Molt bé! Aquest era el resultat: {resultat}")
    else: 
        print(f"T'has equivocat! Aquest era el resultat: {resultat}")

#Truquem a la funció.
exercici()

