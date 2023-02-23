def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds ins {age_seconds}.")


# user_age_in_seconds()


# do not reuse names for function
# do not reuse names for variables in and out functions
# do not use a function before it is defined

def add(x, y):
    print(x + y)


# keyword argument: a=x,b=y
add(x="John", y="Smith")


# default parameter:
def sub(x, y=8):
    print(x - y)


sub(7)
sub(0,4)
sub(x=9,y=3)