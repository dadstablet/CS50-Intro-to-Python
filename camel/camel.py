x = str(input("camelCase: "))

for char in x:
    if char.islower() == False:
        lower_char = char.lower()
        snake_char = "_"+lower_char
        char = snake_char
    store = [char]

print(store)
