class Task:

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if new_name != self.name:
            self.name = new_name
            return self.name

        return "Name cannot be the same."

    def change_due_date(self, new_due_date: str) -> str:
        if new_due_date != self.due_date:
            self.due_date = new_due_date
            return self.due_date

        return "Date cannot be the same."

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        try:
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        except IndexError:
            return "Cannot find comment."

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"



