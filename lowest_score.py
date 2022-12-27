if __name__ == '__main__':
    scores = []
    data = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        data.append([name, score])

    g = sorted(list(set(scores)))[1]

    data.sort()
    for i in data:
        if i[1] == g:
            print(i[0])
            
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
