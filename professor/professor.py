import random


def main():
    user_level = get_level()
    print(generate_integer(user_level))


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
    try:
        if level == 1:
            return random.randint(1, 9)
            # Y = random.randint(1, 9)
        elif level == 2:
            return random.randint(10, 99)
            # Y = random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
            # Y = random.randint(100, 999)
        else:
            return random.randint(1000,9999)
    except ValueError:
        return 'u trash'


if __name__ == "__main__":
    main()
