class Vehicle:

    number_of_wheels = 4

    def __init__(self, make, model, fuel="gas") -> None:
        self.make = make
        self.model = model
        self.fuel = fuel

daily_driver = Vehicle("Subaru", "Crosstrek")
daily_driver.number_of_wheels = 3
print(daily_driver)

print(f"I drive a {daily_driver.make} {daily_driver.model}. It runs on {daily_driver.fuel}")
print(f"My {daily_driver.model} has {daily_driver.number_of_wheels} wheels.")

print(f"Most vehicles have {Vehicle.number_of_wheels} wheels.")