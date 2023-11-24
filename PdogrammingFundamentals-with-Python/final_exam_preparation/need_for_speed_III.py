def drive(cars_dict: dict, car, miles: int, fuel: int):
    cars_dict[car][0] += miles
    cars_dict[car][1] -= fuel
    print(f"{car} driven for {miles} kilometers. {fuel} liters of fuel consumed.")
    if cars_dict[car][0] >= 100000:
        del cars_dict[car]
        print(f"Time to sell the {car}!")
    return cars_dict


def refuel(cars_dict: dict, car, fuel: int):
    if cars_dict[car][1] + fuel > 75:
        fuel = 75 - cars_dict[car][1]
    cars_dict[car][1] += fuel
    print(f"{car} refueled with {fuel} liters")
    return cars_dict


def revert(cars_dict: dict, car, km: int):
    cars_dict[car][0] -= km
    if cars_dict[car][0] < 10000:
        cars_dict[car][0] = 10000
    else:
        print(f"{car} mileage decreased by {km} kilometers")


number_of_cars = int(input())
cars_dictionary = {}
for current_car in range(number_of_cars):
    car_info = input().split('|')
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    cars_dictionary[car] = [mileage, fuel]

while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        break
    car = command[1]
    if command[0] == 'Drive':
        distance = int(command[2])
        fuel_needed = int(command[3])
        if cars_dictionary[car][1] >= fuel_needed:
            drive(cars_dictionary, car, distance, fuel_needed)
        else:
            print("Not enough fuel to make that ride")
    elif command[0] == 'Refuel':
        fuel = int(command[2])
        refuel(cars_dictionary, car, fuel)

    elif command[0] == 'Revert':
        kilometers = int(command[2])
        revert(cars_dictionary, car, kilometers)

for car_name, car_info in cars_dictionary.items():
    print(f"{car_name} -> Mileage: {car_info[0]} kms, Fuel in the tank: {car_info[1]} lt.")