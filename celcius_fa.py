choice=input("Choose temp to change cel to far(1) or far to cel(2) or for both (3) : ")
try:
    choice=int(choice)
except:
    print("Enter number............please")
    exit()
if(choice==1):
    c=float(input("Enter temp into celcius : "))
    temp=(c*9/5)+32
    print(f'temp in far : {temp}')
elif(choice==2):
     f=float(input("Enter temp into far : "))
     temp=(f-32)*5/9
     print(f'temp in cel : {temp}')
elif(choice==3):
     c=float(input("Enter temp into celcius : "))
     temp=(c*9/5)+32
     f=float(input("Enter temp into far : "))
     temp1=(f-32)*5/9
     print(f'temp in cel : {temp}')
     print(f'temp in far : {temp1}')
else:
    print('please enter a valid choice................' )



