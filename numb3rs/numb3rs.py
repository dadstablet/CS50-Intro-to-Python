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
                raise Exception("Invalid. Cannot lead with 0")
            elif int(x) > 255:
                raise Exception("Invalid. Cannot be >255")
        return "Valid"
    except ValueError:
        sys.exit("Value Error")
    # else:
    #     return match.group(1)


...


if __name__ == "__main__":
    main()
