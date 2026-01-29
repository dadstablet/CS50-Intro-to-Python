from datetime import date, timedelta
import sys
import inflect

inflect = inflect.engine()


def main():
    try:
        print(age_in_days(input("Date of Birth: ")))
    except ValueError:
        "Invalid Date"

def age_in_days(birth):
    if date.fromisoformat(birth):
        diff = date.today() - date.fromisoformat(birth)
        diff = diff.days * 24 * 60
        diff_words = inflect.number_to_words(diff)
        return f"{diff_words.capitalize()} minutes"
    else:
        pass
        # raise ValueError

...


if __name__ == "__main__":
    main()
