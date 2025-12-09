import random

def main():
    try:
        x = int(input("Level: "))
        check(x)
    except:
        main()

def check(a):
    answer = random.randint(1, a)
    if a == answer:
        print("Just right!")
    elif a < answer:
        print("Too small!")
    elif a > answer:
        print("Too large!")

main()

