import random as r
print("**************Welcome to Popular game known as Stone Paper and scissor*********************")
print("**********************Due you know the rules of the game??******************")
ch=input("(Press yes or no) : ")
flag=2
ch=ch.lower()
if(ch=='yes'):
    flag=0
elif(ch=='no'):
    flag=1
else:
    print("invalid choice")
    exit()

if(flag==1):
    print("******manual for game ******")
    print("This game is design for computer v/s you...")
    print("Rule 1: if Computer choosen 'Stone' and player choosen 'Stone' then 'Tie' ")
    print("Rule 2: if Computer choosen 'Paper' and player choosen 'Paper' then 'Tie' ")
    print("Rule 3: if Computer choosen 'Scissor' and player choosen 'Scissor' then 'Tie' ")

    print("Rule 4: if Computer choosen 'Stone' and player choosen 'Scissor' then 'Computer Wins' ")
    print("Rule 5: if Computer choosen 'Paper' and player choosen 'Stone' then 'Computer Wins' ")
    print("Rule 6: if Computer choosen 'Scissor' and player choosen 'Paper' then 'Computer Wins' ")

    print("Rule 7: if Computer choosen 'Paper' and player choosen 'Scissor' then 'Player Wins' ")
    print("Rule 8: if Computer choosen 'Scissor' and player choosen 'Stone' then 'Player Wins' ")
    print("Rule 9: if Computer choosen 'Stone' and player choosen 'Paper' then 'Player Wins' ")

    print("********End*********")
    print("********End*********")
com_opt=['stone','paper','scissor']
opt=r.choice(com_opt)
print(opt)
print("Are You ready to play..you will get 3 chances to play :")
for i in range(0,3):
    com_opt=['stone','paper','scissor']
    opt=r.choice(com_opt)
    #print(opt)
    pl_opt=str(input("Enter Stone or Paper or Scissor: "))
    pl_opt=pl_opt.lower()
    #print(pl_opt)
    if(opt=='stone'and pl_opt=='stone'):
        print("*********Tie************")
    elif(opt=='paper'and pl_opt=='paper'):
        print("*********Tie************")
    elif(opt=='scissor'and pl_opt=='scissor'):
        print("*********Tie************")
    elif(opt=='stone'and pl_opt=='scissor'):
        print("*****Computer Wins******")
    elif(opt=='paper'and pl_opt=='stone'):
        print("*****Computer Wins******")
    elif(opt=='scissor'and pl_opt=='paper'):
        print("*****Computer Wins******")
    elif(opt=='paper'and pl_opt=='scissor'):
        print("******Player Wins*******")
    elif(opt=='stone'and pl_opt=='paper'):
        print("******Player Wins*******")
    elif(opt=='scissor'and pl_opt=='stone'):
        print("******Player Wins*******")
    else:
        print("Invalid input")

    
    
    
    
    
    
