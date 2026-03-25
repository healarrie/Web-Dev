x = int(input())

arr_str = input().split()

arr = []
for s in arr_str:
    arr.append(int(s))

for num in arr:
    if num%2==0:
        print(num, end=" ")