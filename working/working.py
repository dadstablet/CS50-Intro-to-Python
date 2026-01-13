import re
import sys

convert_time = {
    "12 am" : "00"
}

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # re.search(r"9:00 AM to 5:00 PM",s)
    try:
        time = re.search(r"^([1-2]?[0-9]){1}:?([0-5][0-9])? (am|pm|AM|PM) to ([1-2]?[0-9]){1}:?([0-5][0-9])? (am|pm|AM|PM)$",s)
        start_hour, start_min, start_day, end_hour, end_min, end_day = time.groups()
        return start_hour, start_min, start_day, end_hour, end_min, end_day
    except AttributeError:
        sys.exit("AttributeError")


if __name__ == "__main__":
    main()
