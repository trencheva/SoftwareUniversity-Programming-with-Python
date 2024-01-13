from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()

passed_cars = 0
crash_happen = False

car = input()

while car != 'END':

    if car == 'green':
        time_to_pass = green_light
        while cars:
            if time_to_pass > 0:
                current_car = cars.popleft()
                if len(current_car) <= time_to_pass + free_window:
                    passed_cars += 1
                    time_to_pass -= len(current_car)
                else:
                    symbol = current_car[time_to_pass + free_window]
                    crash_happen = True
                    break
            else:
                break

    else:
        cars.append(car)

    if crash_happen:
        break
    car = input()

if crash_happen:
    print('A crash happened!')
    print(f'{current_car} was hit at {symbol}.')
else:
    print('Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')