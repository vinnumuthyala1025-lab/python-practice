##what is an armstrong number
##an armstrong number is a number which is equal to the sum of the digits risen to the power as the number of digits
##soo an armstrong num is simply to add the digits 

n = int(input("Enter a number: "))
temp = n
count=len(str(n))
total=0
while n>0:
    digit =n%10
    total = total +digit**count
    n=n//10

if total==temp:
    print("Yes")
else:
    print('No')
