class NewStack(object):
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def push(self, val):
        self.stack_size += 1
        self.stack_list.append(val)

    def is_empty(self):
        if self.stack_size == 0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]


class MinStack2:
    def __init__(self):
        self.main_stack = NewStack()
        self.min_stack =