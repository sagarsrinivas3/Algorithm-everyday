# REVERSING A ARRAY
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
j = len(a) - 1

print("INPUT ARRAY    : ", a)

while i < j:
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    i = i + 1
    j = j - 1

print("REVERSED ARRAY : ", a)
