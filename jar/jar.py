class Jar:
    def __init__(self, capacity=12):
        self._capacity = 12
        self._size = 0
        if self._size > capacity:
            raise ValueError
        elif self._size < 0:
            raise ValueError

    def __str__(self):
        return f"{self._size * '🍪'}"

    def deposit(self, n):
        self._size += n
        if n < 0:
            raise ValueError
        if self._size > self._capacity:
            raise ValueError("ValueError")

    def withdraw(self, n):
        self._size -= n
        if n < 0:
            raise ValueError
        if self._size < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
