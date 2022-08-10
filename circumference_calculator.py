#circumference_calculator

def welcome():
    print("So let's calculate?")

welcome()

def Calculate():
    π=3.1415
    opr= input('''Choose your calculation using one of the codes below:
ec to Get the Radius
d to Get the Diameter
cc to Get the Length of the Circumference
ac to Get the Area of the Circumference
''')

    if opr == "ec":
        num1 = int(input("Enter Diameter:"))
        print("D = 2.r")
        print("{} = 2.R".format(num1))
        print("R = {}/2".format(num1))
        print("R = ",num1/2)
    elif opr == "d":
        num1 = int(input("Enter Radius:"))
        print("D = 2.r")
        print("D = {}.2".format(num1))
        print("D = ",num1*2)
    elif opr == "cc":
        num1 = int(input("Enter Radius:"))
        print("C = 2.π.r")
        print("C = 2(3,14).{}".format(num1))
        print("C = 6,28.{}".format(num1))
        print("C = ",2*π*num1)
    elif opr == "ac":
        num1 = int(input("Enter Radius:"))
        print("A = π.r²")
        print("A = 3,14.{}²".format(num1))
        print("A = 3,14.",(num1**2))
        print("A = ",(π*num1**2))
    else:
        print("Invalid code. Try again")
    again()

def again():
    calc_again = input("Would you like to do another calculation?(y/n)")

    if calc_again.upper() =='Y':
        Calculate()
    elif calc_again.upper()=='N':
        print("See you later :)")
    else:
        again()

Calculate()