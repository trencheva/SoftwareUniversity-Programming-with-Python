class sequence_repeat:
    def __init__(self, sequence, num):
        self.sequence = sequence
        self.number = num + 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.number -= 1

        if not self.number:
            raise StopIteration

        self.index += 1
        return self.sequence[self.index % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
