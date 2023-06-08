num=input("enter number=")
try:
    num=int(num)
    if(num%2==0 or num%3==0 or num%7==0):
        print(num,'number is divisible by 2,3 or 7')
    else:
        print(num,'number is not divisible by 2,3 or 7')
except:
    print("wrong input.....")


