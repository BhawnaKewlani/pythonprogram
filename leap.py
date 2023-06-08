n=input("ENTER A YEAR:")
try:
    n=int(n)
except:
    print('please enter a year')
    exit()
if (n%4==0)and(n%100!=0 or n%400==0):
    print(f'Year is leap year: {n}')
else:
     print(f'Year is not a leap year: {n}')