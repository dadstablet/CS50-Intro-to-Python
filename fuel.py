def main():
    x = input("Fraction: ")
    return(fuel(x))


def convert(fraction):
    while True:
        try:
            split = fraction.split("/")
            numer = int(split[0])
            denom = int(split[1])
            percent = int(round((numer/denom)*100))
        except ValueError:
            main()
        except ZeroDivisionError:
            main()
        else:
            return (print(result(percent)))

def gauge(percentage):
    if 0 <= percentage <= 1:
        output = "E"
    elif 99 <= percentage <= 100:
        output = "F"
    elif percentage > 100:
        return main()
    elif percentage < 0:
        return main()
    else:
        output = f"{round(x)}%"
    return(output)

main()
