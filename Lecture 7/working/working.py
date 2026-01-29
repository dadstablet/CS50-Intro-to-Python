import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # re.search(r"9:00 AM to 5:00 PM",s)
    try:
        if " to " in s:
            s_list = s.split(" to ", 1)
        else:
            raise ValueError

        s_list_new = []
        for item in s_list:
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
            if start_min == None:
                start_min = "00"
            else:
                pass
            time = f"{start_hour}:{start_min}"
            s_list_new.append(time)
    except AttributeError: #added because check wants ValueError, not AttributeError
        raise ValueError
    except ValueError:
        sys.exit("ValueError")
    return f"{s_list_new[0]} to {s_list_new[1]}"


if __name__ == "__main__":
    main()
