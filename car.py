import os
import car

def main():
    displayMainMenu()

carInfo=car.Car("2012", "Toyota",)
    

def callAccelerateMethod():
    n=0
    if (n<5):
        speed = float(input("\nEnter your current speed"))
        car.accelerate(speed)
        car.get_speed()
        n+=1

def callBrakeMethod():
    i=0
    if (i<5):
        speed = float(input("\nEnter your current speed"))
        Car.brake(speed)
        Car.get_speed()
        i+=1

def exitProgram():
    print("Test completed, thank you")
    exit()

def displayMainMenu():
    os.system("cls")
    print ("Welcome to the car test program")
    print("What would you like to do? ")
    print("1. Car information")
    print("2. Accelerate")
    print("3. Brake")
    print("4. Exit")
    sel = int(input("\nEnter your selection"))
    validationSelection(sel)

def validationSelection(sel):
    if (sel == 1):
        Car.__init__(year_model, make, speed)
        print("Press any key to continue")
        displayMainMenu()
    elif (sel == 2):
        callAccelerateMethod()
        print("Press any key to continue")
        displayMainMenu()
    elif (sel == 3):
        callBrakeMethod()
        print("Press any key to continue")
        displayMainMenu()
    elif (sel == 4):
        exitProgram()
main()
