from validator_collection import validators
import sys

def main():
    usr_email = input("Email: ")
    try:
        validators.email(usr_email)
        return usr_email
    except:
        sys.exit("invalid email")

if __name__ == "__main__":
    main()
