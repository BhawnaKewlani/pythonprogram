n=input("Enter a number to check pos or neg or zero: ")
try:
    n=int(n)
except:
    print("Enter a number......")
    exit()
if(n==0):
    print(f'Number is zero {n}')
elif(n>0):
     print(f'Number is positive {n}')
else:
     print(f'Number is negative {n}')
    
