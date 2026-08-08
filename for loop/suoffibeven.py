n = int(input("Enter a number: "))

a = 0
b = 1
total = 0

while a <= n:
    if a % 2 == 0:
        total += a

    c = a + b
    a = b
    b = c

print("Sum of even Fibonacci numbers:", total)