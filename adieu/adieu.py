name_list = []

while True:
    try:
        x = input("Name: ")
        name_list.append(x)
    except EOFError:
        break

for name in name_list:
    

output = print(f"Adieu, adieu, to {name_list}")
