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
