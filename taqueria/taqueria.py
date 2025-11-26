menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# def main():
#     x = input("Item: ")
#     return tally(x)

def tally():
    while True:
        try:
            x = input("Item: ")
            if _ == 0:
                cost = float((menu[x.title()]))
                print(f"${cost}")
            else:
                cost = cost + float((menu[x.title()]))
                print(f"${cost}")
            _ = _ + 1
        except KeyError:
            print("Key Error")

tally()
