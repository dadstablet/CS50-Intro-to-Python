x = str(input("camelCase: "))

def snake(user_input):
    for char in user_input:
        if char.islower() == False:
            lower_char = char.lower()
            snake_char = "_"+lower_char
            char = snake_char

snake(x)
