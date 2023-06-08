unit=input('Enter number of unit consumed:')
try:
    unit=int(unit)
    flag=1
except:
    flag=0
    print('.........wrong input......')
if flag==1:   
    if(unit<=200):
        unit=unit*1.5
        print('bill of rs',unit)
    elif  unit<=350:  
       div=unit-200
       unit=(div*2.5)+(200*1.5)
       print('bill of rs',unit)
    elif unit<=500: 
        div=unit-350
        unit=(div*4)+(150*2.5)+(200*1.5)
        print('bill of rs',unit)
    elif unit>500:
        div=unit-500
        unit=(div*6)+(150*4)+(150*2.5)+(200*1.5)
        print('bill of rs',unit)
    else:
        print("no number entered")
