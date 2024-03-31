from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        used_battery_percentage = round(100 * (mileage / self.max_mileage))
        self.battery_level -= used_battery_percentage



