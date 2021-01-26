# BINARY SEARCH

def binary_search(arr, elem, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if elem == arr[mid]:
        return mid
    elif elem < arr[mid]:
        return binary_search(arr, elem, 0, mid - 1)
    elif elem > arr[mid]:
        return binary_search(arr, elem, mid + 1, high)


a = [1, 2, 3, 4, 5, 6, 7]
elem = 2
low = 0
high = len(a) - 1
pos = binary_search(a, elem, low, high)
if pos == -1:
    print("ELEMENT IS NOT PRESENT")
else:
    print("ELEMENT IS PRESENT IN {} POSITION".format(pos + 1))
