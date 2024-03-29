class User:

    def __init__(self, _id: int, username: str):
        self.user_id = _id
        self.username = username
        self.books = []

    def info(self) -> str:
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

