import sys

def main():
    x = sys.argv[1]
    check(x)

def check(f):
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
