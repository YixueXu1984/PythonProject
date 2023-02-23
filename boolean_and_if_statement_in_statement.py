friends = ["John","Snow"]
abroad = ["John", "Snow"]

#The contents are the same for both lists, thus == will print true
# print(friends == abroad)
# #The lists are different, thus is will print false
# print(friends is abroad)

#case_insensitive_coding
# day_of_week = input("What day of the week is it today?").lower()
#
# if day_of_week == "monday":
#     print("Have a great start of your week!")
# elif day_of_week == "sunday":
#     print("Last chance to have fun!")
# else:
#     print("Full speed ahead!")


#in statement: string, sets, tuples, lists

movies_watched = {"The Matrix", "The Dark Knight", "Hugo"}
user_movie = input("Enter something you've watched recently:")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched it yet!")