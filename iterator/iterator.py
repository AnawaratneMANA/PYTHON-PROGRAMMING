# Iterator method in Python
a = ["apple","mango", "banana"]
itr = iter(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr)) # exception.

itr = reversed(a)
print(next(itr))

# This Integrated in the for loop in Python.