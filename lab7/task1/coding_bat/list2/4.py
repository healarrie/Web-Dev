def sum67(nums):
    total = 0
    ignore = False
    for n in nums:
        if n == 6:
            ignore = True
        if not ignore:
            total += n
        if n == 7 and ignore:
            ignore = False
    return total