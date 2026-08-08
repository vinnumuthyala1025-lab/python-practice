
num = int(input("Enter the number:"))
reverse=0

while num>0:
    digit = num%10

    num=num//10
    reverse = reverse*10+digit
print("The reverse of the number is:", reverse)



