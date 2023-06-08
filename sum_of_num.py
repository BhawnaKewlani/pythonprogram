n=input("Enter number till where you want to enter :")
try:
    n=int(n)
except:
    print("Please enter a valid no............")
    exit()
sum=0
for i in range(0,n):
    x=int(input(f"Value at {i+1} : "))
    sum+=x
print("Sum of values : ",sum)