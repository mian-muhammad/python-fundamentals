class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print(f"Your {self.make} {self.model} is started. Vroom vroom!")
        else:
            print("Your {self.make} {self.model} is started is broken :(")


my_car = Car("Ford", "Thunderbird")
my_car.start()
print(f"Cars have {Car.get_number_of_wheels()} wheels.")
my_car.number_of_wheels = 6
print(f"My car has {my_car.number_of_wheels} wheels.")
print(f"My car has {my_car.get_number_of_wheels()} wheels.")

print(type(my_car))

# The isinstance() function takes an object and a class, and returns True if the object you pass it is an instance of the class.
print("isinstance")
print(isinstance(42, int))
print(isinstance("Hello, World!", str))
print(isinstance(my_car, float))
print(isinstance(my_car, Car))
print(isinstance(False, bool))

# The issubclass function takes two classes, and returns True if the first class is a subclass of the second.
print("issubclass")
print(issubclass(bool, int))
print(issubclass(int, object))
print(issubclass(bool, object))

# __str__ and __repr__
print(f"This object is a {str(my_car)}")
print(f"This object is a {repr(my_car)}")