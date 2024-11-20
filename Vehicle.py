#Parent Class
class Vehicle:
    wheels = 4 #class lvl attribute assigned to all objects from the class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # instance meathod that 
    def __str__(self):
        #return a string representing the vehicle object
        return f"Vehicle: {self.make}, Model: {self.model}, Year: {self.year}"