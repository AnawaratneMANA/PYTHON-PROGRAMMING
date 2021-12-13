# shot cut list
numbers = [1,2,3,4,5]
even = []
for i in numbers:
    if i%2 == 0:
        even.append(i)

even = [i for i in numbers if i%2 == 0]

print("Created List : " , even)