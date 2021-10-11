from collections import deque

cars = deque()

green_light = int(input())
free_window = int(input())
passed_cars = 0
crashed = False

while not crashed:
    line = input()
    if line == "END":
        break

    if line == "green":
        current_green_line = green_light

        while cars and current_green_line > 0:
            car = cars.popleft()

            if current_green_line >= len(car) or \
                    current_green_line + free_window >= len(car):
                passed_cars += 1
                current_green_line -= len(car)
            else:
                print("A crash happened!")
                print(f"{car} was hit at {car[current_green_line + free_window]}.")
                crashed = True
                break
    else:
        cars.append(line)

if not crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
