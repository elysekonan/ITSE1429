# def Employee Class
class Employee:

    # init Method
    def __init__(self, employeeName, employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber 

    # mutators method for Employee class's data
    # attribute
    def set_employeeName(self, employeeName):
        self.__employeeName = employeeName

    def set_employeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber

    # accessors for Employee class's data 
    # attribute
    def get_employeeName(self):
        return self.__employeeName
    
    def get_employeeNumber(self):
        return self.__employeeNumber
