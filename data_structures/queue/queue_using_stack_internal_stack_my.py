# Driver code
class Queue:
    def __init__(self):
        self.s = []

    def enQueue(self, param):
        self.s.append(param)

    def deQueue(self):
        if len(self.s) <= 0:
            print("Queue is empty")
            return
        temp = self.s.pop()

        if len(self.s) <= 0:
            return temp

        item = self.deQueue()

        self.s.append(temp)

        return item




if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
