import math

def normal_method(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

def square_root_method(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num))):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

num = int(input("Enter a number : "))
while True:
    print("1.SIMPLE METHOD 2.SQUARE ROOT METHOD 3.INBUILT FUNCTION")
    choice = input("Enter the choice : ")
    if choice == '1':
        normal_method(num)
    elif choice == '2':
        square_root_method(num)

