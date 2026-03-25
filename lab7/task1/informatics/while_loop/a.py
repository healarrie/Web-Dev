import math
a = int(input())
i = 1
while i <= a:
    if math.isqrt(i)**2==i:
        print(i, end=" ")
    i+=1