a = [1, 90, 3, 20, 5, 6, 7]
print(a)
max = a[-1]
for i, e in reversed(list(enumerate(a))):
    if max < a[i]:
        max = a[i]
    else:
        a[i] = max
print(a)
