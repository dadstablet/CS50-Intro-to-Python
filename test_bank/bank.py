def main():
    x = input("Greeting: ")
    print(f"${value(x)}")

def value(greeting):
    try:
        clean_greeting = greeting.strip().lower()
        if clean_greeting.startswith("hello"): prize = 0
        else:
            if clean_greeting.startswith("h"): prize = 20
            else: prize = 100
        return prize
    except ValueError:
        return 100

if __name__ == "__main__":
    main()


