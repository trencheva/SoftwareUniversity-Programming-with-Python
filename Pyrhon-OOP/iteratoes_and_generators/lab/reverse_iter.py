class reverse_iter:

    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.index = len(self.iter_obj)

    def __iter__(self):
        return self

    def __next__(self):

        if self.index > 0:
            self.index -= 1
            return self.iter_obj[self.index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
