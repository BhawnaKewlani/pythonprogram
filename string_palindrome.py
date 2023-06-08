'''str=input("Enter a String : ")
str2=str[::-1]  #Slicing of string
if(str==str2):
    print(f'String is plaindrome {str} {str2}')
else:
    print(f'String is not a plaindrome {str} {str2}')'''

# how to do it without slicing
'''str=input("Enter a String : ")
str2=''
for i in str:
    str2=i+str2
if(str==str2):
    print(f'String is plaindrome {str} {str2}')
else:
    print(f'String is not a plaindrome {str} {str2}')'''
#predefine fun
str=input("Enter a String : ")
str2=''.join(reversed(str))
print(str2)
