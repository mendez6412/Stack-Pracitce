class InvalidCapacity(Exception):
    pass


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass


class Stack:
    def __init__(self, capacity=10, values=None):
        if not isinstance(values, list):
            values = []
        elif len(values) > capacity:
            raise StackOverflow
        self.values = values
        self.capacity = capacity
        if self.capacity < 1:
            raise InvalidCapacity

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        return (self.values == other.values and self.capacity == other.capacity)

    def __str__(self):
        return "Capacity: {} | Values: {}".format(self.capacity, self.values)

    def is_empty(self):
        return len(self) == 0

    def push(self, value):
        if len(self) >= self.capacity:
            raise StackOverflow

        self.values.append(value)

    def pop(self):
        if len(self) < 1:
            raise StackUnderflow

        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def find(self, value):
        try:
            return self.values.index(value)
        except ValueError:
            return None
