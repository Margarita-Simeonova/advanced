stack = input().split()

reversed_stack = []

while stack:
    el = stack.pop()
    reversed_stack.append(el)

print(" ".join(reversed_stack))
