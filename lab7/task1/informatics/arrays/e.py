x = int(input())

arr_str = input().split()

arr = []
for s in arr_str:
    arr.append(int(s))

found = False

for i in range(1, x):
    if arr[i] * arr[i-1]>0:
        found = True
        break
if found:
    print("YES")
else:
    print("NO")