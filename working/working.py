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
        time = re.search(r"^([1]?[0-9]){1}:?([0-5][0-9])? (am|pm|AM|PM) to ([1]?[0-9]){1}:?([0-5][0-9])? (am|pm|AM|PM)$",s)
        start_hour, start_min, start_day, end_hour, end_min, end_day = time.groups()
        if start_day.lower() == "am":
            if int(start_hour) < 10:
                start_hour = "0"+start_hour
            elif 10 < int(start_hour) < 12:
                start_hour = start_hour
            elif int(start_hour) == 12:
                start_hour = "00"
        elif start_day.lower() == "pm":
            if int(start_hour) == 12:
                start_hour = "12"
            elif int(start_hour) < 12:
                start_hour = start_hour+12

        return f"{start_hour}:{start_min} {start_day.upper()}"
        # return time.groups()
    except AttributeError:
        sys.exit("AttributeError")


if __name__ == "__main__":
    main()
