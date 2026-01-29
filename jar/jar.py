class Jar:
    def __init__(self, capacity=0):
        self._capacity = capacity

    def __str__(self):
        return f"{self._capacity * '🍪'}"

    def deposit(self, n):
        self._capacity += n
        if self._capacity > 12:
            raise ValueError
        elif n < 0:
            raise ValueError

    def withdraw(self, n):
        self._capacity -= n
        if self._capacity < 0:
            raise ValueError
        elif n < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capcity

    @property
    def size(self):
        pass
