months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    x = input("Month: ")
    try:
        x_list = x.split("/")
        year_corrected = int(x_list[2])
        month_corrected = int(x_list[1])
        day_corrected = int(x_list[0])
    except IndexError:
        try:
            x_list = x.split(" ")
            year_corrected = int(x_list[2])
            month_corrected = months[x_list[0]]
            day_corrected = int(x_list[1].strip(","))
        except IndexError:
            main()
        except KeyError:
            main()
    print(f"{year_corrected}-{month_corrected:02}-{day_corrected:02}")

main()
