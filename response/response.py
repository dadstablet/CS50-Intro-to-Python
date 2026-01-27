from validator_collection import validators
import sys

def main():
    usr_email = input("Email: ")
    if validators.email(usr_email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
