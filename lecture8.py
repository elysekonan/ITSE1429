#Lecture 8 implementation program
import car
import os

#main function
def main():
    os.system('cls')
    getCarValue(car)
    exit()


def getCarValue(car):
    year = input('What year is your car?: ')
    make = input('What is the make?: ')
    door = input('How many doors?: ')
    color = input('What is the color of the car?: ')

    #create car object
    myCar = car.Automobile(year, make, door, color)
    
    #Display values entered
    print('Here are the values your entered')
    print('================================')
    print('Make: {0}'.format(myCar.get_make()))
    print('Year: {0}'.format(myCar.get_year()))
    print('Doors: {0}'.format(myCar.get_doors()))
    print('Color: {0}'.format(myCar.get_color()))


#Exit program
def exit():
    print('========================')
    print('Program completed')
    print('========================')

#call main function
main()