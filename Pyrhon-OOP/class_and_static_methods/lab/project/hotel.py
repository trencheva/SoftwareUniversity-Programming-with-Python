from project import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        people = room.guests
        result = room.free_room()

        if not result:
            self.guests -= people

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests" \
                f"\nFree rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}" \
                f"\nTaken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"


