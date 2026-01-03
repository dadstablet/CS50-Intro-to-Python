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
    ip_split = ip.split(".")
    return ip_split


...


if __name__ == "__main__":
    main()
