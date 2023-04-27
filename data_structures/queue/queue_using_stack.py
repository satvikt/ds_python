# Driver code
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, param):
        while len(self.s1) is not 0:
           self.s2.append(self.s1.pop())

        self.s1.append(param)

        while len(self.s2) is not 0:
            self.s1.append(self.s2.pop())

    def deQueue(self):
        return self.s1.pop()


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())