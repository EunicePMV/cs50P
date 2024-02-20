class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError
        self.capacity = capacity

    def __str__(self):
        cookies = ''
        for n in self.capacity:
            cookies += '🍪'
        return cookies

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

jar = Jar(1)
