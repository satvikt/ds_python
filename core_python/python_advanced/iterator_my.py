class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            power = 2**self.n
            self.n += 1
            return power
        else:
            raise StopIteration

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2**n
        n += 1


if __name__ == "__main__":
    # pow = iter(PowTwo(4))
    #
    # print(next(pow))
    # print(next(pow))
    # print(next(pow))
    # print(next(pow))
    # print(next(pow))
    pow = PowTwoGen(3)
    for i in pow:
        print(i)