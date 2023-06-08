s=int(input("Enter the start of table : "))
e=int(input("Enter the end of table : "))
for i in range(s,e+1):
    for j in range(1,11):
        print(j*i," ",end='')
    print()