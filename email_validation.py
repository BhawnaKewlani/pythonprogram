email=input('Enter your Email-id:')
try:
   if type(email)==str:
    flag=1
except:
    print('......invalid input......')
    flag=0
if flag==1:
    if email=='@':  #thinking of logic
        print('ok')
    else:
        print('nope')



