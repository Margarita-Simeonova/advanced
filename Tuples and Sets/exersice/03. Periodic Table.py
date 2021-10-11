n = int(input())

elements_set = set()

for _ in range(n):
    [elements_set.add(x) for x in input().split()]

[print(el) for el in elements_set]
