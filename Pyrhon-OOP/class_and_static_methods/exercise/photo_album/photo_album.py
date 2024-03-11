from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    SYMBOL_COUNT = 11
    SYMBOL = '-'

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for i in range(len(self.photos)):
            if len(self.photos[i]) < PhotoAlbum.PHOTOS_PER_PAGE:
                slot = len(self.photos[i]) + 1
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {slot}"

        return "No more free slots"

    def display(self) -> str:
        result = [f"{PhotoAlbum.SYMBOL_COUNT * PhotoAlbum.SYMBOL}"]
        for page in self.photos:
            result.append(('[] ' * len(page)).strip())
            result.append(f"{PhotoAlbum.SYMBOL_COUNT * PhotoAlbum.SYMBOL}")

        return '\n'.join(result)

