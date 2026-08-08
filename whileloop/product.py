
num = int(input("Enter the number:"))
product = 1
while num>0:
    digit = num %10
    product = product*digit
    num = num//10

print("the product of the digits is =",product)

