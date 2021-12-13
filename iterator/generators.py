# generators.
def remote_control_next():
    yield "one"
    yield "two"


itr = remote_control_next()
next(itr)
next(itr)

# for loop compatible with generators.
for c in remote_control_next():
    print(c)

# fibonachi series.
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
for f in fib():
    if f > 13:
        break
    print(f)