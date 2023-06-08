print ('Hello welcome to guessing no. game!!!!')
print('before we procede further plz fill requirments:')
name=input('Enter your name:')
age=input('Enter your age:')
age=int(age)
if(age>18):
    print('Welcome to game')
    hint=input('do you want hints?????')
    hint=hint.lower()
    if(hint=='yes'):
        print('''ok, no. is of 2 digit....also having 2 facotors only, one is 5 (which is prime),another is also a prime no....but can't tell ;] but second no. is also a 2 digit no ''')
        num=input('Guess the no=')
        num=int(num)
    else:
            print('ok')






else:
    print('Sorry you are not eligable')