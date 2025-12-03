from pyfiglet import Figlet
import sys
import random

if len(sys.argv) == 2:
    # f_input = sys.argv[1]
    font_name = sys.argv[2]
elif len(sys.argv) == 0:
    font_name = "random"

x = input("Input: ")
f = pyfiglet.figlet_format(x)
print(f)

