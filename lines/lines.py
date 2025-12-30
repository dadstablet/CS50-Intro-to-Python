import sys

def main():
    check_file()

def check_file():
    x = sys.argv[:]
    if ".py" in x[1]:
        return x[1]
    elif x.count() > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Not a Python file")

def line_count(f):
    try:
        line_count = 0
        with open(f, "r") as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    line_count += 0
                else:
                    line_count += 1
            return line_count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
