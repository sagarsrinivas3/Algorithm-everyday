# Rotation of array using reversal technique

arr = []
try:
    n = int(input("ENTER NUMBER OF ELEMENTS TO INSERT : "))
    print("Enter ", n, " numbers or charters")
    for i in range(n):
        arr.append(input())
    r = int(input("ENTER NUMBER OF ROTATIONS : "))

except:
    print("ENTER ONLY NUMBERS AS INPUT")

print("INPUT ARRAY ", arr)


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


i = 0
j = n - r - 1
k = n - 1
# Reverse 0 to n-r

while i < j:
    arr[i], arr[j] = swap(arr[i], arr[j])
    i = i + 1
    j = j - 1

# Reversed n-r to n
j = j = n - r

while j < k:
    arr[j], arr[k] = swap(arr[j], arr[k])
    j = j + 1
    k = k - 1

# reversed 0 to n
original_i = 0
original_j = n - 1

while original_i < original_j:
    arr[original_i], arr[original_j] = swap(arr[original_i], arr[original_j])
    original_i = original_i + 1
    original_j = original_j - 1

print("ROTATED ARRAY ", arr)
