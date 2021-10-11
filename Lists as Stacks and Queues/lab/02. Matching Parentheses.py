my_string = input()

stack = []

for index in range(len(my_string)):
    if my_string[index] == "(":
        stack.append(index)
    elif my_string[index] == ")":
        start_index = stack.pop()
        print(my_string[start_index: index + 1])
