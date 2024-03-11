from project import Animal
from project import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.workers: list[Worker] = []
        self.animals: list[Animal] = []

    @staticmethod
    def amount_finder(info, a_or_w_type):
        animal_or_worker_list = []
        for animal_or_worker in info:
            if animal_or_worker.__class__.__name__ == a_or_w_type:
                animal_or_worker_list.append(animal_or_worker)
        return animal_or_worker_list

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        needed_money_to_pay = sum([w.salary for w in self.workers])
        if self.__budget >= needed_money_to_pay:
            self.__budget -= needed_money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        needed_money_to_tend = sum([a.money_for_care for a in self.animals])
        if self.__budget >= needed_money_to_tend:
            self.__budget -= needed_money_to_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals"

        total_lions_list = self.amount_finder(self.animals, 'Lion')
        result += f"\n----- {len(total_lions_list)} Lions:"
        for l in total_lions_list:
            result += f"\n{l}"

        total_tigers_list = self.amount_finder(self.animals, 'Tiger')
        result += f"\n----- {len(total_tigers_list)} Tigers:"
        for t in total_tigers_list:
            result += f"\n{t}"

        total_cheetah_list = self.amount_finder(self.animals, 'Cheetah')

        result += f"\n----- {len(total_cheetah_list)} Cheetahs:"
        for c in total_cheetah_list:
            result += f"\n{c}"

        return result

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers"

        total_keepers_list = self.amount_finder(self.workers, 'Keeper')
        result += f"\n----- {len(total_keepers_list)} Keepers:"
        for k in total_keepers_list:
            result += f"\n{k}"

        total_caretakers_list = self.amount_finder(self.workers, 'Caretaker')
        result += f"\n----- {len(total_caretakers_list)} Caretakers:"
        for c in total_caretakers_list:
            result += f"\n{c}"

        total_vets_list = self.amount_finder(self.workers, 'Vet')
        result += f"\n----- {len(total_vets_list)} Vets:"
        for v in total_vets_list:
            result += f"\n{v}"

        return result
