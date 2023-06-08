"""for i in range(10,0,-1):
    print(i)"""

"""for i in reversed(range(0,10)):
    print (i," ",end="")
"""
"""        
   *
  ***
 *****
********
                 """

for i in range(1,5):
    for j in range(3,i-1,-1):
        print(" ",end="") #spaces
    for k in range(1,i+i): 
        print("*",end="") #star
    print()
