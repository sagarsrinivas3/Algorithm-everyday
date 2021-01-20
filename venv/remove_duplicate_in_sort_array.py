# REMOVE DUPLICATES FROM SORTED ARRAY
arr=[]
n = int(input("ENTER NUMBER OF ELEMENT : "))
j=0;
print("ENTER NUMBERS IN ASCENDING ORDER")
for i in range(n):
    print("Enter", i+1 ," Element")
    arr.append(input())
print("INPUT  ", arr)
for i in range(n-1):
    if arr[i] != arr[i+1]:
        arr[j] = arr[i]
        j = j + 1
arr[j] = arr[n-1]
print("OUTPUT ", arr[:j+1])