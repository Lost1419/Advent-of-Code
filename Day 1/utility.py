class Utility:
    def __init__(self):
        with open('inputs.txt', 'r') as file:
            self.inputs = list(map(int, file.read().split("\n")))

    def find_double(self, number):
        for num in self.inputs:
            if (num + number) == 2020:
                return number

    def find_triple(self, number):
        for num in self.inputs:
            for extra in self.inputs:
                if (num + number + extra) == 2020:
                    return number

    def find(self, opration: str, itrator: list):
        if opration.lower() == 'double':
            multiply = map(self.find_double, itrator)
        elif opration.lower() == 'triple':
            multiply = map(self.find_triple, itrator)

        multiply = list(multiply)

        while None in multiply:
            for value in multiply:
                if value is None:
                    multiply.remove(value)

        return multiply

    def result(self, number_1, number_2, number_3=None):
        if number_3 is None:
            return number_1 * number_2
        else:
            return number_1 * number_2 * number_3
