from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self.get_user_by_license_number(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self.get_vehicle_by_plate_number(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        new_route = Route(start_point, end_point, length, len(self.routes) + 1)

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self.get_user_by_license_number(driving_license_number)
        vehicle = self.get_vehicle_by_plate_number(license_plate_number)
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged][:count]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
        for vehicle in sorted_damaged_vehicles:
            vehicle.change_status()
            vehicle.recharge()

        return f"{len(sorted_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ['*** E-Drive-Rent ***']
        result += [str(user) for user in sorted(self.users, key=lambda u: -u.rating)]
        return '\n'.join(result)

    def get_vehicle_by_plate_number(self, license_plate_number):
        try:
            vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        except StopIteration:
            return None
        return vehicle

    def get_user_by_license_number(self, driving_license_number):
        try:
            user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        except StopIteration:
            return None
        return user