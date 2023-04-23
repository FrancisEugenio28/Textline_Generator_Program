#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Textline Generator

import colorama

colorama.init()

#open the source file
with open("myLife.txt", "w") as life_file:
    while True:
        #create an input for th user 
        line_input = input(colorama.Fore.LIGHTCYAN_EX + "Enter a line: ")
        #add a import time for loading effect
        import time
        print(colorama.Back.LIGHTWHITE_EX + "Printing your entered line in the txt file...")
        time.sleep(1)
        print(colorama.Back.LIGHTWHITE_EX + "DONE!")
        life_file.write(line_input + "\n")
        #ask the user if he/she want to add a line
        retry = input(colorama.Back.RESET + "Do you want to add a line? (y/n): ").upper()
        if retry != "Y":
            break
