#n=int(input("enter the value:"))
#n1=n+(n*10+n)+(n*100+n*10+n)  #n*123
#print("result: ",n1)

a=input("input an interger")
s=0
p=""
for i in range(1,int(a)+1):
  p=a*i
  n1=int( p )
  s=s+n1
print (s)
