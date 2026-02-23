import inflect
p = inflect.engine()


name_list = []
while True:
    try:
        x = input("Name: ")
        name_list.append(x)
    except EOFError:
        print()
        break

output_list = p.join(name_list)
print(f"Adieu, adieu, to {output_list}")

