class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("User Defined Exception : ",self.msg)

try:
    raise Accident("Crash between two cars happens")
except Accident as e:
    e.print_exception()
finally:
    print("This is where the clean-up process happens")