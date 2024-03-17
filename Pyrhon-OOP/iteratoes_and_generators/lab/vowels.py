class vowels:

    def __init__(self, string: str):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'y', 'u']
        self.vowels_found = [v for v in self.string if v.lower() in self.vowels]
        self.start_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start_idx += 1
        if self.start_idx < len(self.vowels_found):
            return self.vowels_found[self.start_idx]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

