# the differences between a list and a tuple are...
#   1. a list can change values (mutable) and a tuple cannot (immutable),
#   2. lists use brackets and tuples use parentheses

# Mutable list
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1

print(list_1)
print(list_2)
# change index 0 from History to Art
list_1[0] = "Art"

print(list_1)
print(list_2)
# it changes both!

# Immutable tuple
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)
# change index 0 from History to Art
tuple_1[0] = "Art"

print(tuple_1)
print(tuple_2)
# it returns an error!
