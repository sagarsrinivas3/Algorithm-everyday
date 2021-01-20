# Stack program using list
def push_element(elem) :
        stk.append(elem)

def pop_element():
    if len(stk) <= 0 :
        print("STACK UNDERFLOW")
    else :
        poped_elem = stk.pop()
        print("popped element", poped_elem)

def display():
    print(stk)

stk = []
while True:
    print("===\t 1.PUSH \t 2.POP \t 3.DISPLAY \t 4.EXIT \t===")
    choice = input("ENTER THE CHOICE : ")
    if choice == '1':
        elem = input("ENTER THE ELEMENT : ")
        push_element(elem)
        display()
    elif choice == '2':
        pop_element()
        display()
    elif choice == '3':
        display()
    elif choice == '4':
        exit()


