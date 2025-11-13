def main():
    x = input("What time is it? ")
    convert(x)

def convert(time):
    hours, minutes = time.split(":")
    clock = int(hours) + (int(minutes)/60)
    print(clock)

if __name__ == "__main__":
    main()
