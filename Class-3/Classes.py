# from Classes import Car, ElectricCar
class Car:
    """A simple class to represent a car."""

    amount_car = 0

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel = 0
        Car.amount_car += 1

    def __del__(self):
        print("Object deleted from Car class")
        Car.amount_car -= 1

    def describe_car(self):
        """Return a formatted description of the car."""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """Display the car's current mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Update the odometer reading.
        Reject changes that attempt to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increase the odometer reading by a given amount."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can only increment by a positive number!")

    def add_fuel(self, amount):
        """Add fuel to the car."""
        if amount > 0:
            self.fuel += amount
            print(f"Added {amount} gallons of fuel. Current fuel: {self.fuel} gallons.")
        else:
            print("Fuel amount must be positive!")


# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2022)
my_car2 = Car("Tesla", "Model S", 2023)
my_car3 = Car("BMW", "X5", 2020)
my_car4 = Car("Honda", "Civic", 2019)

print(Car.amount_car)
del my_car2
print(Car.amount_car)


# # Use the methods of the Car class
print(my_car3.describe_car())
my_car.read_odometer()

my_car.update_odometer(1500)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()

my_car.add_fuel(10)


# Demonstrate inheritance by creating a subclass
class ElectricCar(Car):
    """A specialized version of Car for electric vehicles."""

    ElectricCaramount = 0

    def __init__(self, make, model, year, battery_capacity):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        ElectricCar.ElectricCaramount += 1

    def describe_battery(self):
        """Display information about the battery."""
        print(f"This car has a {self.battery_capacity}-kWh battery.")

    def add_fuel(self, amount):
        """Override method to indicate that electric cars don't use fuel."""
        print("This car doesn't need fuel!")

    def __del__(self):
        print("Object deleted from ElectricCar class")
        ElectricCar.ElectricCaramount -= 1


# Create an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model 3", 2023, 75)

print(my_tesla.describe_car())
my_tesla.describe_battery()
print(ElectricCar.ElectricCaramount)
print(Car.amount_car)
my_tesla.add_fuel(10)  # This will use the overridden method
