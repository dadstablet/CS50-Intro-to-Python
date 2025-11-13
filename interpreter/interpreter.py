user_input = input("Expression: ")
user_array = user_input.split(" ")
# print(user_array)
x = int(user_array[0])
z = int(user_array[2])
y = str(user_array[1])

if y == "+": result = round(x + z, 1)
elif y == "-": result = round(x - z, 1)
else: result = "bruh"

print(result)
