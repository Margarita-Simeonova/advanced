my_string = list(input())

string_as_list = []

while len(my_string) > 0:
    string_as_list.append(my_string.pop())

print(f"{''.join(string_as_list)}")
