
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
# insert
courses.insert(0, "Art")
print(courses)
