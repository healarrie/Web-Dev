x = int(input())

arr_str = input().split()

count = 0
arr = []
for s in arr_str:
    arr.append(int(s))

for num in arr:
    if num>0:
        count+=1

print(count)