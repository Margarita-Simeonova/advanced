def is_vip(guest):
    return guest[0].isdigit()


guests = int(input())

guests_list = {input() for _ in range(guests)}

while True:
    command = input()
    if command == "END":
        break
    guests_list.discard(command)

vip_guests = sorted([g for g in guests_list if is_vip(g)])
regular_guests = sorted([g for g in guests_list if not is_vip(g)])

print(len(guests_list))
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]
