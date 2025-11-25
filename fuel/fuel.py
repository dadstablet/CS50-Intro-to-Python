def main():
    x = input("Fraction: ")
    return(separate_input(x))


def separate_input(input):
    numer = int(input[0])
    denom = int(input[2])
    print(numer/denom)

main()
