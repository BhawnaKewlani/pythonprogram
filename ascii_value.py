c=input('Enter Character:')
if len(c)==1:
    value=ord(c)
    print('ascii',value)
    if value>=123 and value<=127:
        print(c,'is brackets') 
    elif value>=97 and value<=122:
        print(c,'is small alphabet') 
    elif value>=65 and value<=90:
        print(c,'is Capital alphabet')
    elif value>=48 and value<=57:
        print(c,'is digit')
    elif value>=0 and value<=47 or value>=58 and value<=64 or value>=91 and value<=96:
        print(c,'is special characters')
else:
    print('.........invalide input.........')

 