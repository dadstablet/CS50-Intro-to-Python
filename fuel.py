def main():
    x = input("Fraction: ")
    return(convert(x))


def convert(fraction):
    while True:
        try:
            split = fraction.split("/")
            X = int(split[0])
            Y = int(split[1])
            percent = int(round((X/Y)*100))
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
        return (print(gauge(percent)))

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
