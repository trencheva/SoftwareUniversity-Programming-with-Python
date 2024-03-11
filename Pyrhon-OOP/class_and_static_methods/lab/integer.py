class Integer:
    ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"

        return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        result = 0
        for i in range(len(value)):
            if i != 0 and Integer.ROMAN[value[i - 1]] < Integer.ROMAN[value[i]]:
                result += Integer.ROMAN[value[i]] - 2 * Integer.ROMAN[value[i - 1]]

            else:
                result += Integer.ROMAN[value[i]]

        return cls(result)

    @classmethod
    def from_string(cls, value: str):
        if isinstance(value, str):
            return cls(int(value))

        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))



