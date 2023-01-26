courses = ["History", "Math", "Physics", "CompSci"]

# find the index number of an item in the list
print(courses.index("CompSci"))

# find out if the item is in the last
print("Art" in courses)
print("CompSci" in courses)

# using a for loop to print individual items
for item in courses:
    print(item)

# you can change the name of item to whatever makes sense
for course in courses:
    print(course)

# you can print an items list WITH index values using the enumerate function
for index, course in enumerate(courses):
    print(index, course)

# start at your list with a different index value
for index, course in enumerate(courses, start=1):
    print(index, course)

# make a string out of a list
course_str = " - ".join(courses)

print(course_str)

# make a list out of a string
course_str = " - ".join(courses)

new_list = course_str.split(" - ")

print(course_str)
print(new_list)
