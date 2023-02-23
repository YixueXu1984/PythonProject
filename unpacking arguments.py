#functions will have a set of arguments when the function is called:

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


print(multiply(1, 3, 5))
print(multiply(-1))


# one can also unpack a list/set to fuction variables by using *
def add(x, y):
    return x + y

nums = [3, 5]
add(*nums)

nums_1 = {"x": 15, "y":25}
#the following two coding styles does the exact same thing
#unpacking dictionary
print(add(x=nums_1["x"], y=nums_1["y"]))
print(add(**nums_1))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided."

print(apply(1,3,6,7,operator="1"))

