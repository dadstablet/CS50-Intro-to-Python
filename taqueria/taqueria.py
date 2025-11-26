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
    loop_count = 0
    while True:
        try:
            x = input("Item: ")
            if loop_count == 0:
                cost = round(float((menu[x.title()])),2)
                print(f"${cost}")
            else:
                cost = cost + round(float((menu[x.title()])),2)
                print(f"${cost}")
            loop_count += 1
        except KeyError:
            print("Key Error")
        except EOFError:
            break

tally()
