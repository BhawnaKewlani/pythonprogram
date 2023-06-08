a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
c=int(input('Enter 3rd number: '))
if((a>b)and(a>c)):
    print(f'1st number is greater: {a}')
elif((b>a)and(b>c)):
    print(f'2nd number is greater: {b}')
elif((c>a)and(c>b)):
    print(f'3rd number is greater: {c}')
else:
    print('some numbers are equal plz try different numbers.......')
