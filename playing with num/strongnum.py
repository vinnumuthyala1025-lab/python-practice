##what is a strong number 
##in case of a strong number the sum of the factorial of the digits is equal to the number itself

n= int(input("Enter your number:"))
temp = n
total = 0
while n>0:
    digit=n%10
    fact = 1
    for i in range(1,digit+1):
        fact *=1
    total+=fact
    n =n//10
    if total ==temp:
        print('Strong number')
    else :
        print('Not a  strong number')
