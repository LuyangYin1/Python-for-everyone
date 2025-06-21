class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "The animal makes a sound."  # The animal makes a sound.


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name, species="Bird")

    def make_sound(self):
        return "Chirp!"


louis = Dog("Louis", "Golden Retriever")
print(louis.name, "is a", louis.species, "of breed", louis.breed)
print("Louis makes a sound:", louis.make_sound())
bootsie = Cat("Bootsy", "Black")
print(bootsie.name, "is a ", bootsie.species, "of color", bootsie.color)
print("Bootsy makes a sound:", bootsie.make_sound())
