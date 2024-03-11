class GetNextIdMixin:

    id = 0

    @classmethod
    def increase_id(cls):
        cls.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id
