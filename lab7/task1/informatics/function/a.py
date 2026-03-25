def find_min(a, b, c, d):
    res = a
    if b<res:
        res = b
    if c<res:
        res = c
    if d<res:
        res = d
    return res

nums = input().split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])
print(find_min(a, b, c, d))