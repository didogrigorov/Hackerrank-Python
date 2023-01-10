from itertools import combinations


def miniMaxSum(arr):
    combos = list(combinations(arr, 4))
    combo_sums = []
    for combo in combos:
        combo_sums.append(sum(combo))

    print(min(combo_sums), max(combo_sums))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

# myalgorithm
