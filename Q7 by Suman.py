num=int(input("Enter a number:"))
sum=0
while(num>0):
    dig=num%10
    sum=sum+dig
    num=num//10
print("The total sum of digits is:",sum)
