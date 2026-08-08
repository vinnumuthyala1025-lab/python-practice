##playing with the digits of a number
num = int(input("Enter a number: "))
count=0
while num > 0:
    digit = num % 10
    count += 1
    num //= 10

print("The number of digits in the number is:", count)