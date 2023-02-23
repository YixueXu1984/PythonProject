class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # when you want to turn a object into a strong
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    # return a string that is easy to reconstruct the original object
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"


# magic method doesn't need to be called
bob = Person("Bob", 35)
print(bob)


