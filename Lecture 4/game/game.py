import random

def set_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def main():
    level = set_level()
    while True:
        try:
            x = int(input("Guess: "))
            if x > 0:
                help = check(level, x)
            if help == "stop":
                break
        except ValueError:
            pass

def check(a, b):
    answer = random.randint(1, a)
    if b == answer:
        print("Just right!")
        return "stop"
    elif b < answer:
        print("Too small!")
    elif b > answer:
        print("Too large!")

main()

