from queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

        self.curr_size = 0

    def push(self, param):
        self.q1.put(param)
        self.curr_size += 1

    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        item = self.q1.get()
        self.curr_size -= 1

        q = self.q1
        self.q1 = self.q2
        self.q2 = q

        return item

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("current size: ", s.curr_size)
    print(s.pop())
    print(s.pop())
    print(s.pop())

    print("current size: ", s.curr_size)
