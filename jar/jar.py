class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        cookies = ''
        for n in self.cookies:
            cookies += '🍪'
        return cookies

    def deposit(self, n):
        if self.cookies + n <= self.capacity:
            self.cookies += n
        else:
            raise ValueError

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

jar = Jar()
