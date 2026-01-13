import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # re.search(r"9:00 AM to 5:00 PM",s)
    time = re.search(r"([1-2]?[0-9](?::[0-5][0-9])?) ([aApPmM]{2})",s)
    start_time, start_day = time.groups()
    return start_time, start_day
...


if __name__ == "__main__":
    main()
