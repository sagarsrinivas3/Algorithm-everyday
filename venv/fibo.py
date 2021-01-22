# FIBONACCI SERIES
first = -1
second = 1
i = 0
try:
    n = int(input("ENTER NUMBERS OF DIGITS : "))
    while i < n:
        total = first + second
        print(total)
        first = second
        second = total
        i = i + 1

except:
    print("ENTER VALID NUMBER")
