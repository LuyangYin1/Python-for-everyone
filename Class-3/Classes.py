"""
Object-Oriented Programming in Python

This module demonstrates fundamental OOP concepts including:
- Class definition and instantiation
- Instance attributes and methods
- Class attributes and methods
- Constructor and destructor methods
- Inheritance and polymorphism
- Method overriding
- Encapsulation principles

The module includes two main classes:
- Car: Base class representing a generic automobile
- ElectricCar: Derived class demonstrating inheritance

Author: Avnit
Date: 2024
"""


class Car:
    """
    A class to represent a generic automobile.
    
    This class demonstrates fundamental OOP concepts including:
    - Instance attributes (make, model, year, odometer_reading, fuel)
    - Class attributes (amount_car - tracks total number of cars)
    - Constructor method (__init__)
    - Destructor method (__del__)
    - Instance methods for car operations
    - Encapsulation through method-based attribute access
    
    Attributes:
        amount_car (int): Class variable tracking total number of Car instances
        make (str): Manufacturer of the car
        model (str): Model name of the car
        year (int): Manufacturing year
        odometer_reading (int): Current mileage on the car
        fuel (float): Current fuel level in gallons
        
    Methods:
        describe_car(): Returns formatted car description
        read_odometer(): Displays current mileage
        update_odometer(mileage): Updates odometer with validation
        increment_odometer(miles): Adds miles to odometer
        add_fuel(amount): Adds fuel to the car
    """

    # Class attribute - shared across all instances
    amount_car = 0

    def __init__(self, make: str, model: str, year: int):
        """
        Initialize car attributes.
        
        Constructor method that sets up a new Car instance.
        Increments the class counter for tracking total cars.
        
        Args:
            make (str): Manufacturer of the car
            model (str): Model name of the car
            year (int): Manufacturing year
            
        Example:
            >>> my_car = Car("Toyota", "Corolla", 2022)
            >>> print(my_car.make)
            Toyota
        """
        # Instance attributes - unique to each instance
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default starting mileage
        self.fuel = 0  # Default starting fuel level
        
        # Increment class counter
        Car.amount_car += 1

    def __del__(self):
        """
        Destructor method called when object is deleted.
        
        Decrements the class counter when a Car instance is destroyed.
        This helps maintain accurate count of active Car objects.
        """
        print("Object deleted from Car class")
        Car.amount_car -= 1

    def describe_car(self) -> str:
        """
        Return a formatted description of the car.
        
        Returns:
            str: Formatted string describing the car (year make model)
            
        Example:
            >>> my_car = Car("Toyota", "Corolla", 2022)
            >>> my_car.describe_car()
            '2022 Toyota Corolla'
        """
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self) -> None:
        """
        Display the car's current mileage.
        
        Prints the current odometer reading to the console.
        This method provides controlled access to the odometer attribute.
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage: int) -> None:
        """
        Update the odometer reading with validation.
        
        This method demonstrates encapsulation by controlling how the
        odometer attribute can be modified. It prevents rolling back
        the odometer (which would be illegal in real life).
        
        Args:
            mileage (int): New mileage reading
            
        Example:
            >>> my_car = Car("Toyota", "Corolla", 2022)
            >>> my_car.update_odometer(1500)
            >>> my_car.read_odometer()
            This car has 1500 miles on it.
            >>> my_car.update_odometer(1000)  # Attempt to roll back
            You can't roll back an odometer!
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles: int) -> None:
        """
        Increase the odometer reading by a given amount.
        
        This method allows adding miles to the odometer (e.g., after a trip).
        It includes validation to ensure only positive values are added.
        
        Args:
            miles (int): Number of miles to add to odometer
            
        Example:
            >>> my_car = Car("Toyota", "Corolla", 2022)
            >>> my_car.increment_odometer(100)
            >>> my_car.read_odometer()
            This car has 100 miles on it.
        """
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can only increment by a positive number!")

    def add_fuel(self, amount: float) -> None:
        """
        Add fuel to the car.
        
        This method demonstrates encapsulation by providing a controlled
        way to modify the fuel level. It includes validation to ensure
        only positive amounts are added.
        
        Args:
            amount (float): Amount of fuel to add in gallons
            
        Example:
            >>> my_car = Car("Toyota", "Corolla", 2022)
            >>> my_car.add_fuel(10.5)
            Added 10.5 gallons of fuel. Current fuel: 10.5 gallons.
        """
        if amount > 0:
            self.fuel += amount
            print(f"Added {amount} gallons of fuel. Current fuel: {self.fuel} gallons.")
        else:
            print("Fuel amount must be positive!")


# Example 1: Creating Car instances
print("=== Example 1: Creating Car Instances ===")
my_car = Car("Toyota", "Corolla", 2022)
my_car2 = Car("Tesla", "Model S", 2023)
my_car3 = Car("BMW", "X5", 2020)
my_car4 = Car("Honda", "Civic", 2019)

print(f"Total cars created: {Car.amount_car}")

# Example 2: Object lifecycle and destructor
print("\n=== Example 2: Object Lifecycle ===")
del my_car2  # This will trigger the destructor
print(f"Total cars after deletion: {Car.amount_car}")

# Example 3: Using Car methods
print("\n=== Example 3: Using Car Methods ===")
print(f"Car description: {my_car3.describe_car()}")
my_car.read_odometer()

my_car.update_odometer(1500)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()

my_car.add_fuel(10)


class ElectricCar(Car):
    """
    A specialized version of Car for electric vehicles.
    
    This class demonstrates inheritance by extending the Car class.
    It shows how to:
    - Inherit from a parent class
    - Call parent class constructor using super()
    - Override parent class methods
    - Add new attributes and methods specific to electric cars
    - Maintain separate class counters for different car types
    
    Attributes:
        ElectricCaramount (int): Class variable tracking total ElectricCar instances
        battery_capacity (float): Battery capacity in kilowatt-hours
        
    Methods:
        describe_battery(): Display battery information
        add_fuel(amount): Overridden method for electric cars
    """

    # Class attribute specific to ElectricCar
    ElectricCaramount = 0

    def __init__(self, make: str, model: str, year: int, battery_capacity: float):
        """
        Initialize attributes of the parent class and electric car.
        
        This constructor demonstrates how to properly initialize a derived class:
        1. Call the parent class constructor using super()
        2. Initialize attributes specific to the derived class
        3. Update class-specific counters
        
        Args:
            make (str): Manufacturer of the car
            model (str): Model name of the car
            year (int): Manufacturing year
            battery_capacity (float): Battery capacity in kWh
            
        Example:
            >>> my_tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
            >>> print(my_tesla.battery_capacity)
            75
        """
        # Call parent class constructor
        super().__init__(make, model, year)
        
        # Initialize ElectricCar-specific attributes
        self.battery_capacity = battery_capacity
        
        # Update ElectricCar counter
        ElectricCar.ElectricCaramount += 1

    def describe_battery(self) -> None:
        """
        Display information about the battery.
        
        This method is specific to electric cars and demonstrates
        how derived classes can have unique functionality.
        
        Example:
            >>> my_tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
            >>> my_tesla.describe_battery()
            This car has a 75-kWh battery.
        """
        print(f"This car has a {self.battery_capacity}-kWh battery.")

    def add_fuel(self, amount: float) -> None:
        """
        Override method to indicate that electric cars don't use fuel.
        
        This method demonstrates method overriding. It replaces the
        parent class's add_fuel method with behavior appropriate
        for electric vehicles.
        
        Args:
            amount (float): Amount of fuel (ignored for electric cars)
            
        Example:
            >>> my_tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
            >>> my_tesla.add_fuel(10)
            This car doesn't need fuel!
        """
        print("This car doesn't need fuel!")

    def __del__(self):
        """
        Destructor method for ElectricCar instances.
        
        Decrements the ElectricCar counter when an instance is destroyed.
        Note: This will also call the parent class destructor.
        """
        print("Object deleted from ElectricCar class")
        ElectricCar.ElectricCaramount -= 1


# Example 4: Inheritance demonstration
print("\n=== Example 4: Inheritance Demonstration ===")
my_tesla = ElectricCar("Tesla", "Model 3", 2023, 75)

print(f"Electric car description: {my_tesla.describe_car()}")
my_tesla.describe_battery()

print(f"Total ElectricCar instances: {ElectricCar.ElectricCaramount}")
print(f"Total Car instances (including ElectricCar): {Car.amount_car}")

# Example 5: Method overriding demonstration
print("\n=== Example 5: Method Overriding ===")
my_tesla.add_fuel(10)  # This will use the overridden method

# Example 6: Polymorphism demonstration
print("\n=== Example 6: Polymorphism ===")
cars = [my_car, my_tesla]  # List containing different car types

for car in cars:
    print(f"Car: {car.describe_car()}")
    car.add_fuel(5)  # Different behavior for each car type
    print()


print("=== Module Complete ===")
print("This module demonstrates Object-Oriented Programming concepts in Python.")
print("Key concepts covered: classes, inheritance, polymorphism, and encapsulation.")
