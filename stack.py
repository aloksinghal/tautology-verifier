class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

    def print_stack(self):
        print self.items
