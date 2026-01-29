class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity

    def __str__(self):
        #for n cookies in jar, return n cookies
        return "{🍪}"

    def deposit(self, n):
        self._capacity += n

    def withdraw(self, n):
        self._capacity -= n

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
