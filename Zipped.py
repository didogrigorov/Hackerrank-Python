students, scores = list(map(int, (input().split())))
students_list = [x for x in range(students)]
total = 0
summed_scores_per_student = [0 for x in range(students)]

for scores in range(1, scores + 1):
    student_scores = list(map(float, input().split()))
    result = list(zip(students_list, student_scores))

    for i in range(len(result)):
        total += result[i][1]
        summed_scores_per_student[i] += total
        total = 0


for item in summed_scores_per_student:
    result = item / scores
    print(f"{result:.2f}")