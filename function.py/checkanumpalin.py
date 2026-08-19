def palindrome(n):
    rev = 0
    temp = n

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return temp == rev

print(palindrome(121))


