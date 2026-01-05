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
    # if match.group(1) <= 255:
    return int(match.group(1))



...


if __name__ == "__main__":
    main()
