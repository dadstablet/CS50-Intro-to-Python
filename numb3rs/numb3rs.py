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
    match = re.search(r"^([0-9]{1,3})\.$",ip)

    if match.group(1).startswith("0") and match.group(1) != "0": #starts with 0. should not pass
        return "Invalid"
    else:
        return match.group(1)


...


if __name__ == "__main__":
    main()
