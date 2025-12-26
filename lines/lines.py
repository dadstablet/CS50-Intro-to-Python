import sys

def main():
    x = sys.argv[1:]
    get_file(x)

def get_file(f):
    file = f.index()

def check(usr_inpt):
    try:
        if usr_inpt :#contains .py and leads to existing file
            pass
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
