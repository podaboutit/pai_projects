
courses = ["History", "Math", "Physics", "CompSci"]
# access one of the list item
print(courses[0])
print(len(courses))
# access last indexed item
print(courses[-1])
# access items up to but not including an indexed item
print(courses[0:2])
# without a first number it assumes you want to start at the beginning
print(courses[:2])
# add a list item to the end of a list
courses.append("Art")
print(courses)
# insert an item at an indexed position
courses.insert(0, "Art")
print(courses)
# list within a list using multiple variable lists
courses_2 = ["Art", "Education"]
courses.insert(0, courses_2)
print(courses)
# but I can still print just my second list by printing at the index position
print(courses[0])
# you can add each of the items in a variable list to another list with .extend
courses.extend(courses_2)
print(courses)
# you can remove items using .remove
courses.remove("Math")
print(courses)
# remove last item from the list (useful in queue or stack situations)
courses.pop()
print(courses)
# you can makes that a variable as well to pull the popped item
popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)
