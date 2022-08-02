#Car sub class
import automobile

class Car(automobile.Automobile):
    #init method
    def __init__(self, year, make, doors, color):
        #init super class
        automobile.Automobile.__init__(self,year,make)

        #init sub class
        self.__doors = doors
        self.__color = color

    #Mutators
    def set_doors(self, doors):
        self.__doors = doors

    def set_colors(self, color):
        self.__color = color
    
    #Accessors
    def get_doors(self):
        return self.__doors
    
    def get_color(self):
        return self.__color
