import random

def main():
    try:
        x = int(input("Level: "))
    except:
        main()
    answer = random.randint(1, x)
    if x == answer:
        print("Just right!")
    elif x < answer:
        print("Too small!")
    elif x > answer:
        print("Too large!")
main()
