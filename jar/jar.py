class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ''
        for n in range(self.size):
            cookies += '🍪'
        return cookies

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Reached maximum capacity")

    def withdraw(self, n):
        if n > self.size or n > self.capacity:
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
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError("Invalid size number")
        self._size = size

jar = Jar()
jar.deposit(10)
print(jar)
print(jar.capacity)
jar.withdraw(5)
print(jar)
