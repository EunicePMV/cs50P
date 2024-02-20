class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        cookies = ''
        for n in range(self.cookies):
            cookies += '🍪'
        return cookies

    def deposit(self, n):
        if self.cookies + n <= self.capacity:
            self.cookies += n
        else:
            raise ValueError("Reached maximum capacity")

    def withdraw(self, n):
        for sel

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity should be positive integer")
        self._capacity = capacity

    @property
    def size(self):
        ...

jar = Jar()
jar.deposit(13)
print(jar)
print(jar.capacity)
