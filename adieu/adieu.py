

while True:
    name_list = []
    try:
        x = input("Name: ")
        name_list = name_list.append(x)
    except EOFError:
        break
    return name_list

output = print(f"Adieu, adieu, to {name_lst}")
