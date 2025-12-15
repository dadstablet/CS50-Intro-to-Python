import random


def main():
    get_level()
    X = random.randint


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        if 1 <= n <= 3:
            print(n)
            break
        else:
            pass

# def generate_integer(level):



if __name__ == "__main__":
    main()
