from graphics import Graphics
from functions import Functions
from colorama import Fore, Back
import sys

Graphics.start()
while True:
    menu = open("./data/Menu.txt")
    print(menu.read() + "\n")
    print("\n")
    menu = input(">")
    if(menu == "1"):
        switcher = input("\t[L] Log QSO \n\t[G] Historical QSOs\n\n")
        if(switcher == "L"):
            Call = input("Callsign: ")
            Date = input("Date: ")
            Freq = input("Frequency: ")
            Grid = input("Location: ")
            print("\n\tQSO Logged with " + Call + "...\n")
            Functions.LogQSO(Call, Date, Freq, Grid)
        if(switcher == "G"):
            Functions.getQSOs()
    if(menu == "2"):
        Switch = input("Would you like to add a new radio? ([y]/[n]): ")
        if(Switch == "y"):
            Radio = input("Radio Model: ")
            Status = input("Status: ")        
            Functions.Radio(Radio, Status)
        else:
            Functions.getRadios()
    if(menu == "3"):
        Functions.hamQRF()
    if(menu == "exit"):
        sys.exit()
