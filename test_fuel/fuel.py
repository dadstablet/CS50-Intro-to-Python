def main():
    x = input("Fraction: ")
    return(convert(x))


def convert(fraction):
    while True:
        try:
            split = fraction.split("/")
            X = int(split[0])
            Y = int(split[1])
            if Y == 0:
                raise ZeroDivisionError("ZeroDivisionError")
            elif X > Y:
                raise ValueError("ValueError")
            else: pass
            percent = int(round((X/Y)*100))
        except ValueError:
            return "ValueError"
        # except ZeroDivisionError:
        #     print("ZeroDivisionError")
        return percent

def gauge(percentage):
    if 0 <= percentage <= 1:
        output = "E"
    elif 99 <= percentage <= 100:
        output = "F"
    elif percentage > 100:
        return ValueError
    elif percentage < 0:
        return ValueError
    else:
        output = f"{round(x)}%"
    return(output)

if __name__ == "__main__":
    main()
