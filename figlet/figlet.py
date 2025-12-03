import pyfiglet
import sys

if len(sys.argv) == 2:
    f_input = sys.argv[1]
    font_name = sys.argv[2]
elif len(sys.argv) == 0:

x = input("Input: ")
f = pyfiglet.figlet_format(x, font=font_name)
print(f)

