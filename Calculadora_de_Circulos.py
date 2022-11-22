#Calculadora de Circulos#

def welcome():
    print("E aí Bora calcular?")

welcome()

def Calculate():
    π=3.1415
    opr = input('''Escolha seu calculo utilizando um dos Codigos abaixo:
ec para Obter o Raio
d para Obter o Diâmetro
cc para Obter o Comprimentro da Circunfêrencia
ac para Obter a Área da Circunferência
''')

    if opr == "ec":
        num1 = int(input("Insira o Diâmetro:"))
        print("D = 2.r")
        print("{} = 2.R".format(num1))
        print("R = {}/2".format(num1))
        print("R = ",num1/2)
    elif opr == "d":
        num1 = int(input("Insira o Raio:"))
        print("D = 2.r")
        print("D = {}.2".format(num1))
        print("D = ",num1*2)
    elif opr == "cc":
        num1 = int(input("Insira o Raio:"))
        print("C = 2.π.r")
        print("C = 2(3,14).{}".format(num1))
        print("C = 6,28.{}".format(num1))
        print("C = ",2*π*num1)
    elif opr == "ac":
        num1 = int(input("Insira o Raio:"))
        print("A = π.r²")
        print("A = 3,14.{}²".format(num1))
        print("A = 3,14.",(num1**2))
        print("A = ",(π*num1**2))
    else:
        print("Codigo Invalido. Tente Novamente")
    again()

def again():
    calc_again = input("Gostaria de fazer outro cálculo?(s/n)")

    if calc_again.upper() =='S':
        Calculate()
    elif calc_again.upper()=='N':
        print("Até Breve :)")
    else:
        again()

Calculate()