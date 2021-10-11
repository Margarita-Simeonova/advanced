clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_rack = 1
current_capacity = rack_capacity

while clothes:
    cloth = clothes[-1]
    if cloth > current_capacity:
        used_rack += 1
        current_capacity = rack_capacity

    else:
        current_capacity -= cloth
        clothes.pop()

print(used_rack)
