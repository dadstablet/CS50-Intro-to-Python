def main():
    x = input("Fraction: ")
    return(fuel(x))


def fuel(input):
    while True:
        try:
            split = input.split("/")
            numer = int(split[0])
            denom = int(split[1])
            percent = int((numer/denom)*100)
        except ValueError:
            main()
        except ZeroDivisionError:
            main()
        else:
            return (print(result(percent)))

def result(x):
    if 0 <= x <= 1:
        output = "E"
    elif 99 <= x <= 100:
        output = "F"
    elif x > 100:
        return main()
    else:
        output = f"{round(x)}%"
    return(output)

main()
