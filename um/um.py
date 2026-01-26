import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_count = re.search(r"um",s)
    ums = 0
    for groups in um_count.groups():
        ums += 1
    return ums
...


if __name__ == "__main__":
    main()
