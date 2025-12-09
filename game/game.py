import random

def main():
    try:
        level = int(input("Level: "))
        x = int(input("Guess: "))
        check(level, x)
    except:
        main()

def check(a, b):
    answer = random.randint(1, a)
    if b == answer:
        print("Just right!")
    elif b < answer:
        print("Too small!")
        main()
    elif b > answer:
        print("Too large!")
        main()

main()

