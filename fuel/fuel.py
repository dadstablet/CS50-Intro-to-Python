def main():
    x = input("Fraction: ")
    return(fuel(x))


def fuel(input):
    while True:
        try:
            numer = int(input[0])
            denom = int(input[2])
            percent = (numer/denom)*100
        except ValueError:
            main()
        except ZeroDivisionError:
            main()
        else:
            if percent == 0:
                output = "E"
                print(output)
                break
            elif percent == 100:
                output = "F"
                print(output)
                break
            elif percent > 100:
                main()
            else:
                output = f"{round(percent)}%"
                print(output)
                break


main()
