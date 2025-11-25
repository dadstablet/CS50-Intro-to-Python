def main():
    x = input("Fraction: ")
    return(separate_input(x))


def separate_input(input):
    while True:
        try:
            numer = int(input[0])
            denom = int(input[2])
            
        except ValueError:

    print(numer/denom)

main()
