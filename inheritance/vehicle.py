class Vehicle:
    def general_usage(self):
        print("General use of Vehicle is to Provide Transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific Use: Commute to work, Vacation with Family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm Motor Cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific Use: Road Trip, Racing")

c = Car()
c.general_usage()
c.specific_usage()

print()

c = MotorCycle()
c.general_usage()
c.specific_usage()