def main():
    x = input("Greeting: ")
    value(x)

def value(greeting):
    clean_greeting = greeting.strip().lower()
    if clean_greeting.startswith("hello"): print("$0")
    else:
        if clean_greeting.startswith("h"): print ("$20")
        else: print("$100")

if __name__ == "__main__":
    main()


