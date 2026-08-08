n = int(input("Enter the number:"))

a=0
b=1

while a<=n:
    largest = a
    c = a+b
    a = b
    b = c

print('largest fib num:',largest)

