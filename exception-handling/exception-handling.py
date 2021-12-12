# Exception Handling in Python.

x= input("Enter Number : ")
y= input("Enter Number : ")

try:
    z = int(x) / int (y)
except ZeroDivisionError as e:
    print("Exception Occured: " , e)
    z = None
except Exception as e:
    print("Exception type : ", type(e).__name__)
    z = None
print("Division is: ", z)