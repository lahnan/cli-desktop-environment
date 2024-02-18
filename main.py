# Notes!
# Want to run need this
# pip install Py-OS
# pip install os-sys
# pip install PythonTurtle
# pip install psutil
# pip install lib-platform
# pip install colorama
# pip install pycopy-colorsys

import os 
import turtle
import colorsys
import colorama
import platform as pf
import shutil

from turtle import *
from colorama import Back, Fore, Style
# Base

while True:
    cwd = os.getcwd() 

    comand = input('cdi ' + cwd + ' ' )

    # commands list

    # GetDirectory
    if comand == 'gd':
        cwd = os.getcwd() 
        print("Current working directory:", cwd) 

    # Clock
    if comand == 'clock':
        os.system("python clock.py")

    # turtle test
    if comand == 'turtle':
        turtle.bgcolor('black')
        t = turtle.Turtle()
        color = ['red', 'dark red']
        for number in range(400):
            t.forward(number+1)
            t.right(89)
            t.pencolor(color[number%2])
        turtle.done()
        print('Complete Running Turtle')
    
    # turtle test-flower
    if comand == 'turtle flower':
        speed(0)
        bgcolor("black")
        h = 0
        for i in range(16):
            for j in range(18):
                c = colorsys.hsv_to_rgb(h, 1, 1)
                color(c)
                h += 0.005
                rt(90)
                circle(150 - j * 6, 90)
                lt(90)
                circle(150 - j * 6, 90)
                rt(180)
            circle(40, 24)
        done()

    # cek free space
    if comand == 'disk' :
        cwd = os.getcwd() 
        total, used, free = shutil.disk_usage("/")
        print(Fore.CYAN + cwd) 
        print(Fore.GREEN + "Total: %d GiB" % (total // (2**30)))
        print(Fore.YELLOW + "Used: %d GiB" % (used // (2**30)))
        print(Fore.RED + "Free: %d GiB" % (free // (2**30)))
        print('')
        print(Style.RESET_ALL)

    #neofetch
    if comand == 'neofetch' :
        print (Fore.RED +             '░░░░░░░░░░░░░░░░░░░░░░░░░░   OS         :',pf.system())
        print (Fore.GREEN +           '░▒▒▒▒▒█████░████░░██░░██░░   Python     :',pf.python_version())
        print (Fore.MAGENTA +         '░▒▒▒▒▒██░░░░█░░██░░░░░░█░░   Build Date :',pf.python_build())
        print (Fore.CYAN +            '░▒▒▒▒▒██░░░░█░░██░██░░░█░░   Device Name:',pf.node())
        print (Fore.YELLOW +          '░▒▒▒▒▒██░░░░█░░██░██░░░█░░   Os Info    :',pf.platform())
        print (Fore.LIGHTMAGENTA_EX + '░▒▒▒▒▒█████░████░░██░░███░                      ')
        print (Fore.BLUE +            '░░░░░░░░░░░░░░░░░░░░░░░░░░   ███████████████████')
        print (Style.RESET_ALL)
        cwd = os.getcwd()

    # package manager
    if comand == 'package -m' :
        print (Fore.GREEN + 'Package : 1')
        print (Fore.GREEN + '=======================================================================')
        print (Fore.GREEN + '|Base : Turtle                                                        |')
        print (Fore.GREEN + '=======================================================================')
        print (Fore.GREEN + '|installed : 1                                                        |')
        print (Fore.GREEN + '=======================================================================')
        print (Fore.RED + 'Install : ccmd ins [package name] [atribute] ')
        print (Style.RESET_ALL)

    # shutdown
    if comand == 'shutdown' :
        print('Shuting Down!')
        break
        exit()

    # simulate
    if comand == 'bsod' :
        print ('')
        print ('=======================================================================')
        print ('=BSOD ERROR============================================================')
        print ('==ERROR CODE : SIMULATION!====================----------===============')
        print ('=============================================||==:v====||==============')
        print ('==============================================----------===============')
        print ('====SIMULATION! SIMULATION! SIMULATION! SIMULATION! SIMULATION! =======')
        print ('=======================================================================')
        print ('=======================================================================')
        print ('===HELP: help.lahnan.net/error=========================================')
        print ('=======================================================================')

# tmp
# ░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░▒▒▒▒▒█████░████░░██░░██░░
# ░▒▒▒▒▒██░░░░█░░██░░░░░░█░░
# ░▒▒▒▒▒██░░░░█░░██░██░░░█░░
# ░▒▒▒▒▒█████░████░░██░░███░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░


