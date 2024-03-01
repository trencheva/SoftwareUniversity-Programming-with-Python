from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library) -> None or str:
        if user not in library.user_records:
            library.user_records.append(user)

        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> None or str:
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        index = library.user_records.index(user)
        user.username = new_username
        library.user_records[index] = user
        return f"Username successfully changed to: {new_username} for user id: {user_id}"

