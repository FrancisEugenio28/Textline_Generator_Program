#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Textline Generator

#open the source file
with open("myLife.txt", "w") as life_file:
    #create an input for th user 
    line_input = input("Enter a line: ")
    #ask the user if he/she want to add a line
    retry = input("Do you want to add a line? (y/n): ")
    if retry != "Y":
        breaks
