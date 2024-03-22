from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult,
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        try:
            new_loan = self.VALID_LOANS[loan_type]()
        except KeyError:
            raise Exception("Invalid loan type!")

        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(self.VALID_CLIENTS[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: type(l) == self.VALID_LOANS[loan_type], self.loans))
        if (type(client) == Student and type(loan) != StudentLoan) or (type(client) == Adult and type(loan) != MortgageLoan):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = len([l.increase_interest_rate() for l in self.loans if self.VALID_LOANS[loan_type] == type(l)])
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = len([client.increase_clients_interest() for client in self.clients if client.interest < min_rate])
        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_granted_loans = []
        for client in self.clients:
            total_granted_loans.extend(client.loans)

        granted_sum = sum(loan.amount for loan in total_granted_loans)
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {sum(c.income for c in self.clients):.2f}\n" \
               f"Granted Loans: {len(total_granted_loans)}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

