def main():
    x = input("Fraction: ")
    return(fuel(x))


def fuel(input):
    while True:
        try:
            numer = int(input[0])
            denom = int(input[2])
            round_per = round(numer/denom)*100
        except ValueError:
            main()
        except ZeroDivisionError:
            main()
        else:
            if round_per == 0:
                output = "E"
            elif round_per == 100:
                output = "F"
            else:
                output = f"{round_per}%"
            print(output)
            break


main()
