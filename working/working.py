import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # re.search(r"9:00 AM to 5:00 PM",s)
    try:
        time = re.search(r"^([1-2]?[0-9]){1}:?([0-5][0-9])? (am|pm|AM|PM) to ([1-2]?[0-9]){1}:?([0-5][0-9])? (am|pm|AM|PM)$",s)
        # start_hour, start_min, end_time, end_day = time.groups()
        return time.groups()
    except AttributeError:
        sys.exit("AttributeError")


if __name__ == "__main__":
    main()
