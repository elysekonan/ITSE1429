import productionworker
import os

worker = ""

# Main Method
def main():
    # clear terminal
    os.system("cls")
    getProductionWorkerInfo(worker)
    displayEmployeeInfo(worker)
    exit()
    
def getProductionWorkerInfo(worker):
    # prompt the user to enter the data
    employeeName = input("Enter your full name: ")
    employeeNumber = input("Enter your employee number: ")
    shift = int(input("Enter your shift, 1 for day and 2 for night: "))
    hourlyPayRate = float(input("Enter your pay rate: "))

    # create productionworker object
    worker = productionworker.productionworker(employeeName, employeeNumber, shift, hourlyPayRate)
    
# Display collected data function
def displayEmployeeInfo(worker):
    print("Employee informations are here: ")
    print("================================")
    print("Full name:{0}".format(worker.get_employeeName()))
    print("Employee number:{0}".format(worker.get_employeeNumber()))
    print("Shift:{0}".format(worker.get_shift()))
    print("Your pay rate:{0}".format(worker.get_hourlyPayRate()))
        
# Exit the program function
def exit():
    print("Program completed succesfully")
    print("======================================================")
# call the main method
main()