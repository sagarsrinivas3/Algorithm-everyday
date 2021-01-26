# LINEAR SEARCH ALGORITHM
def linear_search(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return -1


a = [10, 20, 30, 40, 50]
elem = int(input("ENTER THE ELEMENT TO SEARCH : "))
pos = linear_search(a, elem)
if pos == -1:
    print("ELEMENT IS NOT PRESENT IN ARRAY")
else:
    print("ELEMENT PRESENT AT {} POSITION".format(pos + 1))
