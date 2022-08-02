#import module os
import os

#Declare global variables
courseList=[]
studentList=[]

def mainMenu():
    # call the menu item
    menuItem1()

#Handle menu and user selection
def menuItem1():
    #Clear the screen
    os.system('cls')
    global select1
    print("Welcome to Richland College course registration and management program")
    print("1.Add Course")
    print("2.Manage Course")
    print("3.Display Course")
    print("4.Exit")

def menu2():
    menuItem2()

def menuItem2():
    os.system('cls')
    global select2
    print("1.Back to the main menu")
    print("2.Add student to course")
    print("3.Display students enrolled in course")

def courseRegistration():
    os.system('cls')
    courseList=[]
    yContinue=[1,2]
    courseName=''
    
    while yContinue == 1:        courseName=input("\nEnter the course name: ")
    courseList.append(courseName)
    yContinue=int(input("press 1 to continue or 2 to exit: "))
    if yContinue == 2:
        print("1. Add Course")
        print("2. Exit")
        #selection=int(input("\nEnter your selection please: "))
    else:
        SystemExit()

# Call the main function
mainMenu()

#User selection
select1=[1,2,3,4]
select2=[1,2,3]
select1=int(input("\nEnter your selection: "))
if (select1 == 1):
    courseRegistration()
elif (select1 == 2):
    menuItem2()
    if (select2 == 1):
        mainMenu()
elif (select1 == 3):
    print(courseList)
else:
    SystemExit()
