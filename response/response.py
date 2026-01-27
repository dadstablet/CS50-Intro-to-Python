from validator_collection import validators
import sys

def main():
    usr_email = input("Email: ")
    try:
        validators.email(usr_email)
        print("Valid")
    except validator_collection.errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()
