from data_structures.Stack import MyStack


class MinStack(MyStack):
    def __init__(self):
        super(MinStack, self).__init__()
        self.min_stack = MyStack()

    def push(self, value):
        super(MinStack).push(value)
        self.stack_size += 1
        min_value = self.min_stack.peek()
        if value > min_value:
            self.min_stack.push(min_value)
        else:
            self.min_stack.push(value)

    def pop(self):
        self.min_stack.pop()
        return super(MinStack).pop()

    def get_min(self):
        return self.min_stack.peek()


if __name__ == "__main__" :
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", super.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
