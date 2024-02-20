class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity

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

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        ...

jar = Jar(12)
print(jar.capacity)
