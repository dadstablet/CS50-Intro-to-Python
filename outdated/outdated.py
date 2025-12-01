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
        date_corrected = str(x_list[2]+'-'+x_list[1]+'-'+x_list[0])
        print(date_corrected)
    except IndexError:
        try:
            x_list = x.split(" ")
            date_corrected = x_list[2]+'-'+months[x_list[1]]+'-'+x_list[0]
            print(date_corrected)
        except IndexError:
            print("IndexError")
main()
