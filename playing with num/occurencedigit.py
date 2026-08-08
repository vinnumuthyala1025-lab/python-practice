##how to count how many times a digit is occured in a number
num = int(input("Enter a number: "))
digit=int(input('Enter the digit you want to count:'))
count=0

while num>0:
    last_digit =num%10
    if last_digit==digit:
        count +=1

print("The digit", digit, "occurs", count, "times in the number.")

