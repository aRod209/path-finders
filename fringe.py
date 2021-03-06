class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(0)

    def is_empty(self):
        return len(self.stack) == 0