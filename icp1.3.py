string=raw_input("Enter a string:")
c1=0
c2=0
c3=1
for i in string:
      if(i.isdigit()):
            c1=c1+1
      if(i.isalpha()):
            c2=c2+1
      if(i==' '):
            c3=c3+1
print("The number of digits is:")
print(c1)
print("The number of letters is:")
print(c2)
print("The number of words is")
print(c3)