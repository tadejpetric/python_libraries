"""
Mini library for manipulating different number bases

"""


class number:
    def __init__(self, base):
        self.number = []
        self.base = base

    def set_list(self, number):
        self.number = number

    def set_string(self, string):
        """
        inputs:
            string = numbers, separated by dots
            for example "11.12.1" is BC1 in base 16
        """
        number = list(map(int, string.split('.')))
        if all(number) < self.base and all(number) >= 0:
            self.number = number
        else:
            raise ValueError('Incorrect digits for base ' + self.base)

    def get_string(self):
        for el in range(len(self.number)):
            if el != len(self.number)-1:
                print(self.number[el], end=".")
            else:
                print(self.number[el])

    def ret_convert_base(self, new):
        if new < 1:
            raise ValueError('Base must be a natural number greater than one')
        new_num = []
        temp = 0
        for digit in range(len(self.number)):
            temp += self.number[-digit-1]*self.base**digit
        digit = 0
        while True:
            new_num.append(temp % new)
            temp //= new
            if temp == 0:
                break
        return new_num[::-1]

    def convert_base(self, new):
        self.number = self.ret_convert_base(new)
        self.base = new

    def n_print(self, base=-1):
        if base == -1:
            self.get_string()
