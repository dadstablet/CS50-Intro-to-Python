import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_count = re.search(r"(um)+",s)
    return um_count.groups()
...


if __name__ == "__main__":
    main()
