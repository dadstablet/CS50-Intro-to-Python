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
        print(x_list)
    except SyntaxError:
        pass
