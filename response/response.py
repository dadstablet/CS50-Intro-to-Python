from validator_collection import validators
import sys

def main():
    usr_email = input("Email: ")
    # try:
    validators.email(usr_email)
    return print("Valid")
    # except:
    #     sys.exit("Invalid")

if __name__ == "__main__":
    main()
