from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 2:
    # f_input = sys.argv[1]
    font_name = sys.argv[2]
elif len(sys.argv) == 0:
    random_font =
    font_name =

x = input("Input: ")
f = pyfiglet.figlet_format(x)
print(f)

