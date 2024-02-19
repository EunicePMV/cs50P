class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int):
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

jar = Jar(capacity=-1)
