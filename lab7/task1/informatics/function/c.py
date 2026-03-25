def xor(a, b):
    if a==1 and b==0:
        return True
    elif a == 0 and b == 1:
        return True
    else:
        return False

nums = input().split()
a = int(nums[0])
b = int(nums[1])
if xor(a, b):
    print(1)
else:
    print(0)