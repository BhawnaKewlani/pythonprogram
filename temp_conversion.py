value=input('Enter value:')
unit=input('Enter Unit:')
convert= input('Convert Into:')
try:
    value=int(value)
    unit=unit.lower()
    convert=convert.lower()
    flag=1
except:
    flag=0
    print('.....invalid input.......')
if flag==1:
    if convert=='k' and unit=='c':
        temp=value+273
        print('The temp in ',convert,'of',value,unit,'is',temp )
    elif convert=='k' and unit=='f':
        temp=273+((value-32)/1.8)
        print('The temp in ',convert,'of',value,unit,'is',temp )
    elif convert=='c' and unit=='k':
        temp=value-273
        print('The temp in ',convert,'of',value,unit,'is',temp )
    elif convert=='c' and unit=='f':
        temp=(value-32)/1.8
        print('The temp in ',convert,'of',value,unit,'is',temp )
    elif convert=='f' and unit=='k':
        temp=((value-273)*1.8)+32
        print('The temp in ',convert,'of',value,unit,'is',temp )
    elif convert=='f' and unit=='c':
        temp=(value*1.8)+32
        print('The temp in ',convert,'of',value,unit,'is',temp )
    else:
        print('....Cannot convert......')

    


