import os

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0


    def accelerate(self, speed):
        #add 5 to the speed data attribute

        self.__speed += 5

    def brake(self, speed):
        #this method substract 5 from 
        # the speed data attribute
        self.__speed -= 5

    def get_speed(self):
        #return the current speed
        return self.__speed
