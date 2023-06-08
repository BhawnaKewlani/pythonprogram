n=input("Enter the number : ")
len=len(n)
#print(len)
try:
    n=int(n)
except:
    print("Please enter a valid number")
    exit()
sum=0
div=n
for i in range(0,len):
    rem=div%10
    cub=rem**len
    sum+=cub
    div=div//10
if(n==sum):
    print("armstrong")
else:
    print("not armstrong")
