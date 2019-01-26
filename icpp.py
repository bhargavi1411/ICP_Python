i=int(input("Enter number: "))
reverse=0
while(i>0):
    digit=i%10
    reverse=reverse*10+digit
    i=i/10
print("Reverse of the number:",reverse)