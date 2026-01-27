import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s_list = s.split(" ")
    ums = 0
    for char in s_list:
        if re.search(r"\Wum\W",char):
            ums += 1
        else:
            pass
    return ums
    # return s_list
...


if __name__ == "__main__":
    main()
