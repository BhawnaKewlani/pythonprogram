n=input("Enter the number: ")
try:
    n=int(n)
except:
    print('Please,Enter the number..............and try again')
    exit()
def fact(num):
    if(num<=1):
        return num
    else:
        num=num*fact(num-1)
        return num
f=fact(n)
print(f'Factorial is : {f}')