name_list = []

while True:
    try:
        x = input("Name: ")
        name_list.append(x)
    except EOFError:
        break

count_list = len(name_list)

if n


output = print(f"Adieu, adieu, to {name_list}")
