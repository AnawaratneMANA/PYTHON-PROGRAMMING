# Defining a Class in Python.
class Human:
    def __init__(self, occupation):
        self.name = "Nirmith Akash" # hardcoded values.
        self.occupation = occupation  # parameter values.

    def do_work(self):
        if self.occupation == "Student":
            print(self.name, "Studying")
        elif self.occupation == "Actor":
            print(self.name, "Acting")

    def speak(self):
        print(self.name, "Says How Are you?")

# Creating Object from the Defined Class.
akash = Human("Student")
akash.do_work()
akash.speak()

kamal = Human("Actor")
kamal.do_work()
kamal.speak()
