class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ''
        for n in range(self.cookies):
            cookies += '🍪'
        return cookies

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Reached maximum capacity")

    def withdraw(self, n):
        if self.size - n < self.capacity:
            raise ValueError("Not enough cookies")
        else:
            self.size -= n

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
        return self.size

jar = Jar()
jar.deposit(13)
print(jar)
print(jar.capacity)
