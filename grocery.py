#! python
# Lecture 4 - Chapter 6, read and write to file and exceptions.
import os

#Global variables
groceryFile ='grocery.txt'

#Main function
def main():
    displayMainMenu()


#Display main menu
def displayMainMenu():
    #local variables
    sel = 0
    os.system('cls')
    print('Welcome to my shopping list')
    print('=======================================')
    print('1. Enter groceries')
    print('2. Display groceries')
    print('3. Exit') 
    sel=input("Enter a selection: ")

#Exception handling - checking for value error
    try:
        sel=int(sel)
        validateSelection(sel)
    except ValueError:
        os.system('cls')
        print('Error: You must enter a numeric value.')
        print('=====================================')
        input('Press any key to continue')
        displayMainMenu()    
   

#Validate main menu selection
def validateSelection(sel):
    if (sel == 1):
        groceryDataEntry()
        displayMainMenu()
    elif  (sel ==2):
        displayGroceries()
        displayMainMenu()
    elif (sel == 3):
        exitApplication()
    else:
        displayMainMenu()

#Exit Application
def exitApplication():
    print('==========================')
    print('Program completed!! Thank you.')
    exit()

#Display Groceries
def displayGroceries():
    #open the grocery file

    try:   
        file1 = open(groceryFile, 'r')     
    #read the file
        fileContent = file1.read()     

    #display file content
        print('Stored grocery list')
        print('====================')
        print(fileContent)

        #close the file
        file1.close()
        input('Enter any key to continue')
         
    except IOError:
        os.system('cls')
        #print("Error: Unable to read {0} file from filesystem.".format(groceryFile))
        print('Error: Unable to read' +  groceryFile + 'file from filesystem.')
        print('=====================================')
        input('Press any key to continue')
        displayMainMenu()

#Handle grocery data entry
def groceryDataEntry():
    #local variable
    isContinue = True
    while isContinue:
        groceryValue = input('Enter grocery name: ')
        #save grocery to file
        saveGroceryToFile(groceryValue)
        isContinuePrompt = input('Add another item? y for yes, n for no')
        if (isContinuePrompt == 'n'):
             isContinue = False


#Saves grocery data
def saveGroceryToFile(grocery):
    # Open grocery list file
    file1 = open(groceryFile,'a')

    #write to file
    file1.write(grocery + '\n')

    #close file 
    file1.close

#Program entry point
main()