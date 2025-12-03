from pyfiglet import Figlet
import sys

f_input = sys.argv[1]
font_name = sys.argv[2]

x = input("Input: ")

f = pyfiglet.figlet_format(x, font="slant")
print(f)
