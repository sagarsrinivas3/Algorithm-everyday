a = [1, 5, 10, 15, 20]
b = [1, 2, 4, 6, 7, 40, 80, 90]

i = 0
j = 0
k = 0
r = []

print("ARRAY 1 : ", a)
print("ARRAY 2 : ", b)
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        r.append(a[i])
        i = i + 1
    elif a[i] == b[j]:
        r.append(a[i])
        i = i + 1
        j = j + 1
    else:
        r.append(b[j])
        j = j + 1

while i < len(a):
    r.append(a[i])
    i = i + 1
while j < len(b):
    r.append(b[j])
    j = j + 1

print("MERGED ARRAY : ", r)