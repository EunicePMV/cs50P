from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

try:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            text = input('Input: ')
            print(f'Output: \n{figlet.renderText(text)}')
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
except IndexError:
    random_font = choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    text = input('Input: ')
    print(f'Output: \n{figlet.renderText(text)}')
