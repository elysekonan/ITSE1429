import employee

# def a subclass of Employee class
class productionworker (employee.Employee):

    worker = ("Barbara Senders", "837465", 1, 15.25)
    # init method
    def __init__(self, employeeName, employeeNumber, shift, hourlyPayRate):
        employee.Employee.__init__(self, employeeName, employeeNumber)
        self.__hourlyPayRate = hourlyPayRate
        self.shift = [1,2]

    # mutators for ProductionWorker class's data's
    # attribute
    def set_shift(self, shift):
        self.shift = [1,2]
    def set_hourlyPayRate(self, hourlyPayRate):
        self.hourlyPayRate = hourlyPayRate

    # mutators for ProductionWorker class's 
    # data attribute
    def get_shift(self):
        return self.shift
    def get_hourlyPayRate(self):
        return self.__hourlyPayRate