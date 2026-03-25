n = int(input())
arr = [int(s) for s in input().split()]

first_max = -10**10
second_max = -10**10

for score in arr:
    if score > first_max:
        second_max = first_max
        first_max = score
    elif score > second_max and score != first_max:
        second_max = score

print(second_max)