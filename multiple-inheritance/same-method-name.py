class Father():
    def skills(self):
        print("I enjoy Gardening")

class Mother():
    def skills(self):
        print("I enjoy Cooking")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I enjoy Sports")

c = Child()
c.skills()
