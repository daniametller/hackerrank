def getNumOnTimeStudents(studentList):
    studentList.sort()
    i = 0
    on_time_counter = int(0)
    for i in range(0, len(studentList)):
        if studentList[i] <=0:
            on_time_counter += 1
        else:
            return on_time_counter
    return on_time_counter

num_cases =int(input())
for i in range(0, num_cases):
    num_students, min_on_time_needed = input().split()
    num_students, min_on_time_needed = int(num_students), int(min_on_time_needed)
    studentList = [int(numeric_string) for numeric_string in input().split()]
    if min_on_time_needed <= getNumOnTimeStudents(studentList):
        print("NO")
    else:
        print("YES")
