import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # if re.search(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",ip):
    #     return "True"
    # has to be 0-255. cannot be 001
    re.search(r"[0-2]2
    else:
        return "False"


...


if __name__ == "__main__":
    main()
