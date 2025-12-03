name_list = []

while True:
    try:
        x = input("Name: ")
        name_list = name_list.append(x)
    except EOFError:
        break

output = print(f"Adieu, adieu, to {x}")
