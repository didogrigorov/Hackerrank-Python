def is_palindrome(n):
    x = n
    y = 0

    palindrome = lambda a, z: (a * 10) + z % 10

    while x > 0:
        x, y = x // 10, palindrome(y,x)

    return y == n

print(is_palindrome(12121))