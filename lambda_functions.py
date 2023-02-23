# Lambda functions are functions that doesn't have a name, and only used to return values.
# Lambda functions are exclusively used to operate on iputs and return outputs.

def add(x, y):
    return x + y


add_lambda = lambda x, y: x + y

print(add_lambda(5, 7))
print(add(5, 7))

# Another example of lambda functions in coding practice:

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
# list comprehension:
doubled_0 = [double(x) for x in sequence]
#map: slower than list comprehension, but common in other coding languages, style and consistancy for large project
doubled_1 = list(map(double, sequence))

# list comprehension with lambda functions:
doubled_2 = [(lambda x: x * 2)(x) for x in sequence]
# map with lambda functions:
doubled_3 = list(map(lambda x: x * 2, sequence))