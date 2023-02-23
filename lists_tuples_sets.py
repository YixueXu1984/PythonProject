# lists can be edited, has order
list = ["Abel","Bob","Carol"]
# tuples cannot be edited, has order
tuple = ("Abel",)
# set can be edited but cannot have duplicates, doesn't have order
set = {"Abel","Bob","Carol"}

list.append("Smith")
list.remove("Bob")
set.add("Smith")
set.remove("Bob")
print(tuple)


friends = {"John","Noel","Sara","Susan","Alice"}
abroad = {"John","Noel","Alice"}
#difference can produce a set of elements from set A that is not in set B
local_friends = friends.difference(abroad)
print(local_friends)
#union can join two sets together
print(local_friends.union(abroad))
#intersection can produce the intesections of set A and set B
arts = {"A","B","C","D"}
science = {"A","C","E","F"}
both = arts.intersection(science)
print(both)