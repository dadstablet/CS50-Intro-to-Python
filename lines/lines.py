import sys

def main():
    x = sys.argv[:]
    use_file = check_file(x)
    print(line_count(use_file))

def check_file(f):
    if len(f) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" in f[1]:
        return f[1]
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
