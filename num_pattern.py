'''1
   1 2
   1 2 3
   1 2 3 4'''

'''n=int(input("Enter the number : "))
for  i in  range(1,n+1):
    for j in range(1,i+1):
        print(j," ",end='')
    print()'''

'''1
   2 2
   3 3 3 
   4 4 4 4'''

'''n=int(input("Enter the number : "))
for  i in  range(1,n+1):
    for j in range(1,i+1):
        print(i," ",end='')
    print()'''

'''1
   2 3
   4 5 6 
   7 8 9 10'''

'''n=int(input("Enter the number : "))
c=1
for  i in  range(1,n+1):
    for j in range(1,i+1):
        print(c," ",end='')
        c+=1
    print()'''

'''   *
     ***
    *****
   ******* '''

n=int(input("Enter the number : "))
for  i in  range(1,n+1):
    for j in range(n+1,0,-1):
        print("*",end='')
    print()
