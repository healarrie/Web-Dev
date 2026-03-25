a = int(input())
i = 1
while i <= a:
    if 2**i<a:
        print(2**i, end= " ")
    i += 1