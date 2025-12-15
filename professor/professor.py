import random


def main():
    user_level = get_level()
    generate_integer(user_level)
    

def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        if 1 <= n <= 3:
            return n
        else:
            pass


def generate_integer(level):
    if level == 1:
        return [random.randint(1, 9), random.randint(1, 9)]
    elif level == 2:
        return [random.randint(10, 99), random.randint(10, 99)]
    elif level == 3:
        return [random.randint(100, 999), random.randint(10, 99)]
    else:
        raise ValueError


if __name__ == "__main__":
    main()
