import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums = 0
    for char in s:
        re.search(r"(um)",char)
    return um_count.groups()
...


if __name__ == "__main__":
    main()
