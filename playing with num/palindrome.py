##palindrome


num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if original == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    


















