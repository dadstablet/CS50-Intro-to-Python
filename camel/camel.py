x = str(input("camelCase: "))

for char in x:
    if char.islower() == False:
        lower_char = char.lower()
        snake_char = "_"+lower_char
        print(snake_char, end="")
