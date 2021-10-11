first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    line_args = input().split()
    command = line_args[0]
    command_parameter = line_args[1]

    if command == "Add" and command_parameter == "First":
        [first_set.add(int(x)) for x in line_args[2:]]

    elif command == "Add" and command_parameter == "Second":
        [second_set.add(int(x)) for x in line_args[2:]]

    elif command == "Remove" and command_parameter == "First":
        current_set = [int(x) for x in line_args[2:]]
        first_set = first_set.difference(current_set)

    elif command == "Remove" and command_parameter == "Second":
        current_set = [int(x) for x in line_args[2:]]
        second_set = second_set.difference(current_set)

    else:
        print(first_set.issubset(second_set)
              or second_set.issubset(first_set))

print(", ".join(str(x) for x in sorted(first_set)))
print(", ".join(str(x) for x in sorted(second_set)))
