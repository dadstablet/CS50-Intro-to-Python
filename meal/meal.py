def main():
    x = input("What time is it? ")
    convert(x)

def convert(time):
    hours, minutes = time.split(":")
    sum_hr_min = float(int(hours) + (int(minutes)/60))
    if 7 <= sum_hr_min <= 8: print("breakfast time")
    elif 12 <= sum_hr_min <= 13: print("lunch time")
    elif 18 <= sum_hr_min <= 19: print("dinner time")

if __name__ == "__main__":
    main()
