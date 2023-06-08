n=int(input("Enter a number to check prime or not : "))
flag=0
if(n<=1):
    print(f"Invalid number",n)
    exit()
else:
    for i in range(2,n-1):
        if(n%i==0):
            flag=1
            break
        else:
            flag=0           
if(flag==1):
    print(f"Number is not prime......{n}")
else:
    print(f"Number is prime....{n}")