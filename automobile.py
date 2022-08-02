#Automobile - super class

class Automobile:

    #define init method
    def __init__(self, year,make):
        self.__year = year
        self.__make = make
    
    #Mutators methods
    def set_year(self, year):
        self.__year = year

    def set_make(self, make):
        self.__make = make
    
    #Accesors 
    def get_year(self):
        return self.__year
    
    def get_make(self):
        return self.__make