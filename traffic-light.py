# traffic light color meaning
color= input("enter one traffic color=")
if type(color)==str :
    color=color.lower()
    if(color=='red'or color=='Red' or color=='RED'):
        print("red means stop")
    elif color=='yellow'or color=='Yellow' or color=='YELLOW':
        print ('yellow means get ready')
    elif color=='green'or color=='Green'or color=='GREEN':
        print("green means go")
    else:
        print("wrong color of choice")
