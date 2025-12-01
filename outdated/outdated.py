months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    x = input("Month: ")
    try:
        x_list = x.split("/")
        date_corrected = str(x_list[2]+'-'+x_list[1]+'-'+x_list[0])
        print(date_corrected)
    except IndexError:
        try:
            x_list = x.

main()
