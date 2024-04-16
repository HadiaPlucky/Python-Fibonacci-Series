n=int(input("How many Fibonacci Numbers do you want to print\n"))
if(n==0):
    print("No fibonacci number at zeroth position")
elif(n==1):
    print("0")


a=0
b=1
print(a)
print(b)

for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)


