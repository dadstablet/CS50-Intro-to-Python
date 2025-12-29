import sys

def main():
    x = sys.argv[1]
    check(x)

def check(f):
    try:
        with open(f, "r") as file:
            for line in file:
                if line.startswith
                line_count += count(line)
        return line_count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
