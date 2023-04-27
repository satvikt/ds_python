class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            res = 2 ** self.n
            self.n += 1
            return res
        else:
            raise StopIteration

def PowTwoGen(max):
    n = 0
    while n < max:
        yield 2**n
        n += 1

def main():
    powers = PowTwo(3)

    i = iter(powers)

    # Using next to get to the next iterator element
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

main()


