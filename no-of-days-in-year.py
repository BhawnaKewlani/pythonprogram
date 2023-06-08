year= input('Enter Year =')
month= input('Enter Month=')
day= input('Enter Day=')
try:
    year=int(year)
    month=int(month)
    day=int(day)
    flag=1
except:
    flag=0
    print('.....sorry it take interger only.....')
if(flag==1):
    if month==1 and day<=31:                            #jan -31
        print ('the no of days is =',day)
    elif month==2 and day<=28:                          #FEB=28
        sum=31+day
        print ('the no of days is =',sum)
    elif month==3 and day<=31:                          #MAR=31
        sum=31+28+day
        print ('the no of days is =',sum)
    elif month==4 and day<=30:                          #april=30
        sum=31+28+31+day
        print ('the no of days is =',sum)
    elif month==5 and day<=31:                          #may=31
        sum=31+28+31+30+day
        print ('the no of days is =',sum)
    elif month==6 and day<=30:                          #june30
        sum=31+28+31+30+31+day
        print ('the no of days is =',sum)
    elif month==7 and day<=31:                          #july31
        sum=31+28+31+30+31+30+day
        print ('the no of days is =',sum)
    elif month==8 and day<=31:                          #aug=31
        sum=31+28+31+30+31+30+31+day
        print ('the no of days is =',sum)
    elif month==9 and day<=30:                          #SEP30
        sum=31+28+31+30+31+30+31+31+day
        print ('the no of days is =',sum)
    elif month==10 and day<=31:                         #oct31
        sum=31+28+31+30+31+30+31+31+30+day
        print ('the no of days is =',sum)
    elif month==11 and day<=30:                         #nov=30
        sum=31+28+31+30+31+30+31+31+30+31+day
        print ('the no of days is =',sum)
    elif month==12 and day<=31:                         #dec=31
        sum=31+28+31+30+31+30+31+31+30+31+30+day
        print ('the no of days is =',sum)
    else:
        print('.....wrong selected.....')
    
    
    
        



