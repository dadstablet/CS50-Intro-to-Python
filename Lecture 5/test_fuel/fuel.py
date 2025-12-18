def main():
    x = input("Fraction: ")
    return(convert(x))


def convert(fraction):
    while True:
        split = fraction.split("/")
        X = int(split[0])
        Y = int(split[1])
        if Y == 0:
            raise ZeroDivisionError
        elif X > Y:
            raise ValueError
        elif X < 0:
            raise ValueError
        elif Y < 0:
            raise ValueError
        else:
            pass
        try:
            percent = int(round((X/Y)*100))
            return percent
        except ValueError:
            return "ValueError"

def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            output = "E"
        elif 99 <= percentage <= 100:
            output = "F"
        elif 1 < percentage < 99:
            output = f"{round(int(percentage))}%"
        else:
            raise ValueError
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"
    return(output)

if __name__ == "__main__":
    main()
