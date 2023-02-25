class ClassTest:
    def instance_method(self):
        print(f"Called instant method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")

test = ClassTest()
# two ways of calling instance method
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()
