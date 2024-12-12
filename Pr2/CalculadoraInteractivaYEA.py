#Iniciem la funció
def calculadora():

#Fem un bucle infinit
    while True:

    #Demana els numeros i operador
        num1 = float(input("Posa el primer número:"))
        num2 = float(input("Posa el segon número:"))
        operador = (input("Posa el operador:"))

    #Fes que si el operador es reconeix, es trenqui el bucle, si no, un missatge es veura y es reiniciara el codi
        if (operador == "*"):
            print(num1 * num2)
            break
        elif (operador == "+"):
            print(num1 + num2)
            break
        elif (operador == "-"):
            print(num1 - num2)
            break
        elif (operador == "/"):
            print(num1 / num2)
            break
        elif (operador == "%"):
            print(num1 - num2 / 100 * num1)
            break
        else:
            print("Operador no vàlid, torna-ho a fer si us plau")

#Truca la funció
calculadora()