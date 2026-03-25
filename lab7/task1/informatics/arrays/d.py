x = int(input())

arr_str = input().split()

count = 0
arr = []
for s in arr_str:
    arr.append(int(s))

for i in range(1, x):
    if arr[i]>arr[i-1]:
        count +=1

print(count)