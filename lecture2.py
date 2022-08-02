# Display the course registration menu
print("Welcome to Ricland College Course Registration/Management Program")
print("1. Add Course")
print("2. Exit")

# Making selection
selection = [1,2]
selection=int(input("\nEnter your selection please: "))

# store course name
courseName=[]
yContinue=[1,2]
while selection == 1:
    courseName=input('\nEnter the course name: ')
    print("You enter ",courseName)
    yContinue=int(input("press 1 to continue or 2 to exit: "))
    if yContinue == 1:
        print("1. Add Course")
        print("2. Exit")
        selection=int(input("\nEnter your selection please: "))
    else:
        break

# Exit the menu
else:
    SystemExit()

