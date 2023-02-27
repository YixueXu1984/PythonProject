def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisior cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


# functions in python are variables that can be called
result = calculate(20, 4, operator=divide)
print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Bob Smith", get_friend_name))
