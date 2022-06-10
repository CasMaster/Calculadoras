#Calculadora de Circulos#
def welcome():
    print("E aí Bora calcular?")

welcome()

def Calculate():
    π=3.1415
    operação = input('''Escolha seu calculo utlizando um dos Codigos abaixo:
ec para Obter o Raio
d para Obter o Diâmetro
cc para Obter o Comprimentro da Circunfêrencia
ac para Obter a Área da Circunferência
''')

    if operação == "ec":
        Numero_1 = int(input("Insira o Diâmetro:"))
        print("D=2.r")
        print("{}=2.R=".format(Numero_1))
        print("R={}/2=".format(Numero_1))
        print("R = ",Numero_1/2)
    elif operação == "d":
        Numero_1 = int(input("Insira o Raio:"))
        print("D=2.r")
        print("D={}.2".format(Numero_1))
        print("D = ",Numero_1*2)
    elif operação == "cc":
        Numero_1 = int(input("Insira o Raio:"))
        print("C=2.π.r")
        print("C = 2(3,14).{}".format(Numero_1))
        print("C = 6,28.{}".format(Numero_1))
        print("C = ",2*π*Numero_1)
    elif operação == "ac":
        Numero_1 = int(input("Insira o Raio:"))
        print("A=π.r²")
        print("A = 3,14.{}²".format(Numero_1))
        print("A = 3,14.",(Numero_1**2))
        print("A = ",(π*Numero_1**2))
    else:
        print("Codigo Invalido. Tente Novamente")
    again()

def again():
    calc_again = input("Gostaria de fazer outro cálculo?")

    if calc_again.upper() =='Y':
        Calculate()
    elif calc_again.upper()=='N':
        print("Até Breve :)")
    else:
        again()

Calculate()