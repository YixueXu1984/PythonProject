friends = ["Abel", "Bob","John","Noel"]

for friend in friends:
    print(f"{friend} is my friend.")

for friend in range(4):
    print(f"{friend} is my friend.")


grades = [35,67,98,100,100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)


# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 != 0:
        evens.add(number)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ").lower()
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")