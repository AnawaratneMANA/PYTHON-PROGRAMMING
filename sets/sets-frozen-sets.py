basket = {"orange", "apple", "mango", "apple", "orange"}
print(type(basket))
print(basket)

# Initializing a Set.
a = set()
a.add(1)
a.add(2)

# List into a Set().
numbers = [1, 2, 3, 1, 2, 3]
unique_numbers = set(numbers)
print(unique_numbers)

# Frozen Sets. (It doesn't allow to add new elements.)
fs = frozenset(numbers)
print(fs)