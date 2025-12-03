from pyfiglet import Figlet
import random

figlet = Figlet()

font_list = figlet.getFonts()

print(random.choice(font_list))
