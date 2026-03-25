x = int(input())
arr = [int(s) for s in input().split()]

rev_arr = arr[::-1]

for el in rev_arr:
    print(el, end=" ")