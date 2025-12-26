import sys

def main():
    x = sys.argv[1]
    print(get_file(x))

def get_file(f):
    f_list = f.split(" ")
    return f_list


def check(usr_inpt):
    try:
        if usr_inpt :#contains .py and leads to existing file
            pass
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        sys.exit("File does not exist")
