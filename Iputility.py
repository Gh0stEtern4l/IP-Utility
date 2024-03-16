import sys
import random
import time
import os
import colorama
import fade
import subprocess

def Main():
    ft1 = fade.purplepink(text="""

███████╗ █████╗ ██╗     ██╗     ███████╗███╗   ██╗    ██╗██████╗       ██╗   ██╗████████╗██╗██╗         ███╗   ███╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██║     ██╔════╝████╗  ██║    ██║██╔══██╗      ██║   ██║╚══██╔══╝██║██║         ████╗ ████║██╔═══██╗██╔══██╗
█████╗  ███████║██║     ██║     █████╗  ██╔██╗ ██║    ██║██████╔╝█████╗██║   ██║   ██║   ██║██║         ██╔████╔██║██║   ██║██║  ██║
██╔══╝  ██╔══██║██║     ██║     ██╔══╝  ██║╚██╗██║    ██║██╔═══╝ ╚════╝██║   ██║   ██║   ██║██║         ██║╚██╔╝██║██║   ██║██║  ██║
██║     ██║  ██║███████╗███████╗███████╗██║ ╚████║    ██║██║           ╚██████╔╝   ██║   ██║███████╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝    ╚═╝╚═╝            ╚═════╝    ╚═╝   ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ 
                                                                                                                                                                                                                                                       
                                                                                                           LonelyAngel - Discord.com

""")

    ft2 = fade.pinkred(text="""

                        ╔═════════════════════════╗         ╔═════════════════════════╗
                        ║       LonelyAngel       ║         ║        LonelyAngel      ║
                     ╔═══════════════════════════════╗   ╔═══════════════════════════════╗
                     ║ [1] Your IP Info              ║   ║   [4] Socials                 ║  
                     ║ [2] Erase IP                  ║   ║   [5] Exit                    ║
                     ║ [3] Get new IP (After Erase)  ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
                   
""")
    print(ft1)
    print(ft2)

    choice = input(fade.pinkred(text="Choice one: "))
    if choice == "1":
        subprocess.run("ipconfig", shell=True)
        print()
        print()
        print("IP Info Shown!!")
        print()
        print("in 5 seconds, the console will Reset...")
        time.sleep(5)
        Main()

    if choice == "2":
        subprocess.run("ipconfig release", shell=True)
        print()
        print()
        print("IP Deleted!!")
        print()
        print("in 5 seconds, the console will Reset...")
        time.sleep(5)
        Main()

    if choice == "3":
        subprocess.run("ipconfig renew", shell=True)
        print()
        print()
        print("New IP Generated!!")
        print()
        print("in 5 seconds, the console will Reset...")
        time.sleep(5)
        Main()

    if choice == "4":
        print("loading Socials...")
        time.sleep(5)
        Socials()

    if choice == "5":
        print("Exiting the Console...")
        time.sleep(5)
        exit()



def Socials():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    lst2 = fade.water(text="""

                                           ╔════════════════════════════╗      
                                           ║      dsc.gg/lun4rgh0st     ║  
                                           ╚════════════════════════════╝ 

""")

    lst1 = fade.purpleblue(text="""

███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ███████╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██╔════╝
███████╗██║   ██║██║     ██║███████║██║     ███████╗
╚════██║██║   ██║██║     ██║██╔══██║██║     ╚════██║
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗███████║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

""")
    print(lst1)
    print(lst2)
    Choice = input(fade.pinkred(text="[TIP] type [back] to go back to the main screen..."))
    print()
    if Choice == "back":
        Main()


Main()