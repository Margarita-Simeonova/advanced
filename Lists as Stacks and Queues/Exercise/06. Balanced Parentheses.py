expression = input()

stack = []
balanced = True

for ch in expression:
    if ch in "{[(":
        stack.append(ch)
    else:
        last_open = stack.pop()
        pair = f"{last_open}{ch}"
        if pair not in "()[]{}":
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")
