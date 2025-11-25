def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_first_digit_0(x):
    for char in x:
        if char.isdigit():
            if char == '0':
                return True
            else:
                return False
    return False

def num_between(x):
    num_string = False
    for char in x:
        if char.isdigit():
            num_string = True
        elif char.isalpha():
            if num_string == True:
                return False
    else:
        return True

def is_valid(s):
    if s[:1].isnumeric():
        return False
    elif len(s) > 6:
        return False
    elif len(s) < 2:
        return False
    elif num_between(s) == False:
        return False
    elif is_first_digit_0(s):
        return False
    elif s.isalnum() == False:
        return False
    else:
        return True

main()
