# SWAPPING 2 NUMBERS
def using_temp(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    print("AFTER SWAPPING ", num1, " ", num2)

def without_temp(num1,num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print("AFTER SWAPPING ", num1, " ", num2)


def using_xor(num1,num2):
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    print("AFTER SWAPPING ", num1, " ", num2)


def python_shortcut(num1,num2):
    num1, num2 = num2, num1
    print("AFTER SWAPPING ", num1, " ", num2)


num1 = int(input("Enter a number1 : "))
num2 = int(input("Enter a number2 : "))
while True:
    print("1.USING TEMP VARIABLE \t 2.WITHOUT USING TEMP VARIABLE \t 3.USING XOR \t 4. PYTHON SHORTCUT")
    choice = input("Enter the choice : ")
    print("BEFORE SWAPPING", num1, " ", num2)
    if choice == '1':
        using_temp(num1,num2)
    elif choice == '2':
        without_temp(num1,num2)
    elif choice == '3':
        using_xor(num1,num2)
    elif choice == '4':
        python_shortcut(num1,num2)

