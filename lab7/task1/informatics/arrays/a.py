x = int(input())

arr_str = input().split()

arr = []
for s in arr_str:
    arr.append(int(s))

for i in range(0,x,2):
    print(arr[i], end=" ")