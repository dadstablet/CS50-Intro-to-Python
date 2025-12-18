def main():
    x = input("Fraction: ")
    return(fuel(x))


def convert(fraction):
    while True:
        try:
            split = input.split("/")
            numer = int(split[0])
            denom = int(split[1])
            percent = int(round((numer/denom)*100))
        except ValueError:
            
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
    elif x < 0:
        return main()
    else:
        output = f"{round(x)}%"
    return(output)

main()
