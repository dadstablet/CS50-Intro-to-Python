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
                raise ZeroDivisionError
            elif X > Y:
                raise ValueError
            else: pass
            percent = int(round((X/Y)*100))
        except ValueError:
            return "ValueError"
        except ZeroDivisionError:
            return "ZeroDivisionError"
        # except ZeroDivisionError:
        #     print("ZeroDivisionError")
        return percent

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
