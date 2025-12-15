import random


def main():
    user_level = get_level()
    _ = 0
    score = 0
    while _ < 10:
        X = generate_integer(user_level)
        Y = generate_integer(user_level)
        Q = input(f"{X} + {Y} = ")
        try:
            int_Q = int(Q)
            if int_Q == (X +Y):
                print(Q)
                score += 1
            else:
                print("EEE")
        except ValueError:
            print("EEE")
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
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
