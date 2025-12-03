import pyfiglet
import sys
import random

figlet = pyfiglet.Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    user_font = random.choice(font_list)
elif len(sys.argv) == 3:
    user_font = sys.argv[2]
    if 

x = input("Input: ")
f = pyfiglet.figlet_format(x, font=user_font)
print(f)

