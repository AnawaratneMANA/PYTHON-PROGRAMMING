# Set repeated data will be discarded.
s = set([1,2,3,4,5,6,7,1,2,3])
print(s)

citiets = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]
z = zip (citiets, countries)
print (z)

for a in z:
    print(a)

# create a dictionary. merge the information in two list.
d = {city: contry for city, contry in zip(citiets, countries)}
print (d)