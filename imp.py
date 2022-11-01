import envparse
from tcolors import colorize,Color
from colorama import Back

a = open('options.env','r').read()
b =colorize(a,Color.BLUE)
print(Back.BLACK + b)
