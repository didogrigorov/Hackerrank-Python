import re

user_input = input().rstrip().split()
n = int(user_input[0])
m = int(user_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_message = ""
for j in range(m):
    for i in range(n):
        decoded_message += matrix[i][j]

decoded_script = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded_message)

print(decoded_message)
