from collections import namedtuple

num_students = int(input())
Student = namedtuple('Student', input())
total = 0

for i in range(1, num_students + 1):
    total += int(Student(*input().split()).MARKS)

average = total / num_students
print(f"{average:.2f}")