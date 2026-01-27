
def main():
    print(validate(input("Email: ")))

def validate(e):
    if e.is_email() == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
