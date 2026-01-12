import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # re.search(r/"9:00 AM to 5:00 PM",s)
    re.search(r/"[(?:12)(?:11)(?:10)]",s)

...


if __name__ == "__main__":
    main()
