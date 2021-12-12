class Father():
    def gardening(self):
        print("I enjoy Gardening")

class Mother():
    def cooking(self):
        print("I enjoy Cooking")

class Child(Father, Mother):
    def sports(self):
        print("I enjoy Sports")

c = Child()
c.gardening()
c.cooking()
c.sports()