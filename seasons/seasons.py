from datetime import date, timedelta
import sys
import inflect


def main():
    birth = input("Date of Birth: ")
    if date.fromisoformat(birth):
        diff = date.today() - date.fromisoformat(birth)
        diff = diff.days * 24 * 60
        print(diff)
    else:
        sys.exit("Invalid date")

...


if __name__ == "__main__":
    main()
