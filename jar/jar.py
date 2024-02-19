class Jar:
    def __init__(self, capacity=12):
        if capacity is int:
            self.capacity = capacity
        else:
            raise ValueError

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

jar = Jar(12)
