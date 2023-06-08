def factorial():
    n=int(input("enter a no:"))
    f=n
    if n<0:
         print("Factorial cannot happen")
    elif n==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n):
            f=f*i
    print("fact=",f)
factorial()
            
        
        
    
