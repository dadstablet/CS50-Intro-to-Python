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
        except percent > 100:
            main()
        else:
            return (print(result(percent)))

def result(x):
    if x == 0:
        output = "E"
        print(output)
    elif x == 100:
        output = "F"
        print(output)
    else:
        output = f"{round(x)}%"
        print(output)


main()
