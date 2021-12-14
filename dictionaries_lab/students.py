course_students = {}

command = input()
while ":" in command:
    info = command.split(":")
    name = info[0]
    id = info[1]
    course = info[2]
    if course not in course_students:
        course_students[course] = {}
    course_students[course][id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in course_students.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")