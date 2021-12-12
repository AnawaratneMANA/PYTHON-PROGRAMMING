# Raise a standard exception
try:
    raise MemoryError("Memory Error")
except MemoryError as e: 
    print(e)