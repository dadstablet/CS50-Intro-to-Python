import sys

def main():
    x = sys.argv[1]
    check(x)


def check(f):
    try:
        with open(f, "r") as file:
            if f :#contains .py and leads to existing file
                pass
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()
