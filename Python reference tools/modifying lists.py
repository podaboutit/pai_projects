
courses = ["History", "Math", "Physics", "CompSci"]
# reverse the list
courses.reverse()
print(courses)
# sort the list alphanumerically
courses.sort()
print(courses)
# sort the list in reverse
courses.sort(reverse=True)
print(courses)
# sort the list without altering the first list
sorted_courses = sorted(courses)
print(sorted_courses)
print(courses)
# add,

print(courses.index("CompSci"))
