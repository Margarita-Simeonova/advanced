from collections import deque

substrings = deque(input().split())
main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

collected_colors = []

while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ''
    color = left + right

    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
        continue
    color = right + left

    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
    else:
        left = left[:-1]
        right = right[:-1]

        if left:
            substrings.insert(len(substrings) // 2, left)
        if right:
            substrings.insert(len(substrings) // 2, right)

secondary_colors_required = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"],
}

for color in collected_colors:
    if color in main_colors:
        continue
    required_colors = secondary_colors_required[color]
    is_valid = all([x in collected_colors for x in required_colors])
    if not is_valid:
        collected_colors.remove(color)

print(collected_colors)
