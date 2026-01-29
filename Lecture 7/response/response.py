from validator_collection import validators, errors
import sys

def main():
    usr_email = input("Email: ")
    try:
        validators.email(usr_email)
        print("Valid")
    except validators.errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()
