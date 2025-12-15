import random


def main():
    user_level = get_level()
    _ = 0
    score = 0
    while _ < 10:
        X = generate_integer(user_level)
        Y = generate_integer(user_level)
        errors = 0
        while errors < 3:
            try:
                Q = int(input(f"{X} + {Y} = "))
                if Q == (X + Y):
                    score += 1
                    errors = 100
                else:
                    raise ValueError
            except ValueError:
                errors += 1
                print("EEE")
            if errors == 3:
                print(f"{X} + {Y} = {X+Y}")
        _ += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
            else:
                pass
        except:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
