class Jar:
    def __init__(self, capacity=12):
        if capacity > 12:
            raise ValueError
        elif capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    def __str__(self):
        return f"{self._capacity * 'cookie'}"

    def deposit(self, n):
        self._capacity += n

    def withdraw(self, n):
        self._capacity -= n

    @property
    def capacity(self):
        return self._capcity

    @property
    def size(self):
        pass
