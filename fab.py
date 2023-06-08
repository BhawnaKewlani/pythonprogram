n=input("Enter the number till where you want to print series  : ")
try:
    n=int(n)
except:
    print("Please enter a number...........")
    exit()
f=0
s=1
print("Fabonacci Series : ")
print(f,' ',s,' ',end='')
for i in range(0,n-2):  
    n=f+s
    f=s
    s=n
    print(n,' ',end='')

    

