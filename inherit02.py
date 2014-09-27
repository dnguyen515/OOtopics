__author__ = "on line source"

from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount.
        """
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle.
        """
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)
        
    def repair_cost(self):
        """ set up local variables cost_of_repair, date_of_repair
        ... make these variables of type list so that each time 
        ... a repair occurs, the fact can be retained.
        """
        cost_of_repair = []
        date_of_repair = []
        repairCost = raw_input("Enter cost of the repair: ")
        cost_of_repair.append(repairCost)
        date = raw_input("Enter repair date: ")
        date_of_repair.append(date)
        for x in cost_of_repair:
            print x
        for x in date_of_repair:
            print x
    
    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is.
        """
        pass
        
class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership.
    """

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is.
        """
        return 'car'

class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership.
    """

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is.
        """
        return 'truck'
        
class Motorcycle(Vehicle):
    """A motorcycle for sale by Jeffco Car Dealership.
    """

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is.
        """
        return 'motorcycle'
