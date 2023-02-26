#raise a error in python
def divide(diviend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return diviend / divisor

grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
# e will contain the error
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")