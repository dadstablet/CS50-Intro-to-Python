def main():
    x = input("Fraction: ")
    return(separate_input(x))


def separate_input(input):
    while True:
        try:
            numer = int(input[0])
            denom = int(input[2])
            round_per = round(numer/denom)*100
        except ValueError:
            main()
        else:
            print(f"{round_per}%")
            break

main()
