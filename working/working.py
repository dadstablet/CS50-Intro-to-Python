import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # re.search(r"9:00 AM to 5:00 PM",s)
    try:
        s_list = s.split(" to ", 1)
        # return s_list
    except AttributeError:
        sys.exit("AttributeError")

    for item in s_list:
        try:
            time = re.search(r"^([1]?[0-9]){1}:?([0-5][0-9])? (am|pm|AM|PM)", item)
            start_hour, start_min, start_day = time.groups()
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
                    start_hour = int(start_hour)
                    start_hour = start_hour + 12
            time = f"{start_hour}:{start_min} {start_day.upper()}"
            # return time.groups()
        except AttributeError:
            sys.exit("AttributeError")


if __name__ == "__main__":
    main()
