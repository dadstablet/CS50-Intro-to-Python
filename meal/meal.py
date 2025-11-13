def main():
    x = input("What time is it? ")
    convert(x)
    print(x)
    # if 7 <= x <= 8: print("breakfast time")
    # elif 12 <= x <= 13: print("lunch time")
    # elif 18 <= x <= 19: print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    sum_hr_min = float(int(hours) + (int(minutes)/60))
    return(sum_hr_min)

if __name__ == "__main__":
    main()
