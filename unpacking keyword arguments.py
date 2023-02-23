def named(name, age):
    print(name, age)


def named_0(**kwargs):
    print(kwargs)


# unpack the dictionary into unpacked keyword arguments
details = {"name": "Bob", "age": 25}
named(**details)
named_0(name="Bob", age=25)


def print_nicely(**kwargs):
    named_0(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

# one can use both unpacking in function arguments
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5, name="Bob", age=25)

def myfunction(**kwargs):
    print(kwargs)

myfunction(**"Bob")  # error, must be mapping
myfunction(**None) # error