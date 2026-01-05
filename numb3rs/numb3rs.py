import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # if re.search(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",ip):
    #     return "True"
    # has to be 0-255. cannot be 001
    # else:
    #     return "False"
    try:
        match = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip)
        for x in match.groups():
            if x.startswith("0") and x != "0": #starts with 0. should not pass
                return "Invalid"
            elif int(x) > 255:
                return "Invalid"
            else:
                pass
        return "Valid"
    except AttributeError:
        sys.exit("Invalid")


if __name__ == "__main__":
    main()
