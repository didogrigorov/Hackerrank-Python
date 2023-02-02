def average(array):
    array_set = set(array)

    result = sum(array_set) / len(array_set)

    return result


user_array = list(map(int, input().split()))
print(average(user_array))