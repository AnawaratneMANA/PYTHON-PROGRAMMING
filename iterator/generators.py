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