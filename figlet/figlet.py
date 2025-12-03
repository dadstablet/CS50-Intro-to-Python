import pyfiglet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 2:
    # f_input = sys.argv[1]
    user_font = sys.argv[2]
elif len(sys.argv) == 0:
    user_font = random.choice(font_list)

x = input("Input: ")
f = pyfiglet.figlet_format(x, font=user_font)
print(f)

