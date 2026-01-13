import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # re.search(r"9:00 AM to 5:00 PM",s)
    time = re.search(r"([1-2]?[0-9]:[0-5][0-9]) ()",s)
    start_time = time.group(1)
    return start_time
...


if __name__ == "__main__":
    main()
