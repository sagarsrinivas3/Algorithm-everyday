# array operations only integer
arr = [20, 30, 40, 60, 50, 10, 100]


def insert_at_last(elem):
    print("ELEMENT ", elem, "is inserted at last")
    arr.append(elem)


def delete_at_last():
    deleted_elem = arr.pop()
    print("LAST ELEMENT DELETED : ", deleted_elem)


def insert_at_beginning(elem):
    print("ELEMENT ", elem, "is inserted at beginning")
    arr.insert(0, elem)


def delete_at_beginning():
    del arr[0]


def insert_at_pos(pos, elem):
    arr.insert(pos, elem)


def delete_at_pos(pos):
    del arr[pos]


def remove_elem(elem):
    arr.remove(elem)


while True:
    print(" 1.INSERT AT BEGINNING \n 2.DELETE AT BEGINNING \n 3.INSERT AT LAST \n 4.DELETE AT LAST \n 5.INSERT AT "
          "PARTICULAR POS \n 6.DELETE AT PARTICULAR POS \n 7.REMOVE PARTICULAR ELEM")
    choice = input("ENTER THE CHOICE : ")
    if choice == '1':
        print("\nINITIAL ARRAY", arr)
        elem = int(input("ENTER THE ELEMENT TO INSERT : "))
        insert_at_beginning(elem)
        print("AFTER INSERTING ELEMENT ", arr, "\n\n")
    elif choice == '2':
        print("\nINITIAL ARRAY", arr)
        delete_at_beginning()
        print("AFTER DELETING ELEMENT ", arr, "\n\n")
    elif choice == '3':
        print("\nINITIAL ARRAY", arr)
        elem = int(input("ENTER THE ELEMENT TO INSERT : "))
        insert_at_last(elem)
        print("AFTER INSERTING ELEMENT ", arr, "\n\n")
    elif choice == '4':
        print("\nINITIAL ARRAY", arr)
        delete_at_last()
        print("AFTER DELETING ELEMENT ", arr, "\n\n")
    elif choice == '5':
        print("\nINITIAL ARRAY", arr)
        pos = int(input("ENTER THE POS : "))
        elem = int(input("ENTER THE ELEMENT TO INSERT : "))
        insert_at_pos(pos-1, elem)
        print("AFTER INSERTING ELEMENT ", arr, "\n\n")
    elif choice == '6':
        print("\nINITIAL ARRAY", arr)
        pos = int(input("ENTER THE POS : "))
        delete_at_pos(pos-1)
        print("AFTER DELETING ELEMENT ", arr, "\n\n")
    elif choice == '7':
        print("\nINITIAL ARRAY", arr)
        elem = int(input("ENTER THE ELEMENT TO DELETE : "))
        print(type(elem))
        print(type(arr[1]))
        if elem in arr:
            remove_elem(elem)
            print("AFTER DELETING ELEMENT ", arr, "\n\n")
        else :
            print("THE ELEMENT IS NOT PRESENT IN ARRAY\n\n")


