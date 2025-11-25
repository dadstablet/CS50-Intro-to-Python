def main():
    x = input("Fraction: ")
    return(fuel(x))


def fuel(input):
    while True:
        try:
            numer = int(input[0])
            denom = int(input[2])
            percent = int((numer/denom)*100)
        except ValueError:
            main()
        except ZeroDivisionError:
            main()
        else:
            return (print(result(percent)))

def result(x):
    if x == 0:
        output = "E"
    elif x == 100:
        output = "F"
    elif x > 100:
        return main()
    else:
        output = f"{round(x)}%"
    return(output)

main()
