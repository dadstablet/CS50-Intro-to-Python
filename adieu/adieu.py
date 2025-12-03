import inflect

name_list = []

while True:
    try:
        x = input("Name: ")
        name_list.append(x)
    except EOFError:
        break

output_list = p.join(name_list)

output = print(f"Adieu, adieu, to {output_list}")
