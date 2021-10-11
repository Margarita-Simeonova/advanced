from collections import deque

kids_names = deque(input().split())
count = int(input())

while len(kids_names) > 1:
    kids_names.rotate(-count)
    print(f"Removed {kids_names.pop()}")

print(f"Last is {kids_names.popleft()}")
