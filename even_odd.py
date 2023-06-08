n=input("Enter number to check even odd: ")
try:
   n=int(n)
except:
    print("Please Enter a number.....")
    exit()
if(type(n)==int):
  if(n%2==0):
    print(f'Even: {n}')
  else:
     print(f'Odd: {n}')

  