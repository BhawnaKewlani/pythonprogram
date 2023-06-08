print('''Welcome to the popular game known as Stone , Paper , Scissor''')
print("******Rules are very simple********")
print("1 for STONE")
print("2 for PAPER")
print("3 for SCISSOR")
print("We need exactly 2 players")
player=input("How many player are their???=")
try:
    player=int(player)
    flag=1
except:
    flag=0

if flag==1 and player==2:
    # if(player==2):
    #      print(" You can play the game") #Waht is the role for if their are 2 player then only we can play this if contion is
    # else:
    #      print(" You cannot play the game")
    choice1=input("Player1:\t Enter your choice : ")
    choice1=int(choice1)
    choice2=input("Player2:\t Enter your choice : ")
    choice2=int(choice2)
    if(choice1==1 and choice2==1 ):
         print ("Tie")
    elif(choice1==2 and choice2==2 ):
        print ("Tie")
    elif(choice1==3 and choice2==3 ):
        print ("Tie")
    elif(choice1==1 and choice2==2 ):
        print ("PLAYER2 WINS")
    elif(choice1==1 and choice2==3 ):
        print ("PLAYER1 WINS")
    elif(choice1==2 and choice2==1 ):
        print ("PLAYER1 WINS")
    elif(choice1==2 and choice2==3 ):
        print ("PLAYER2 WINS")
    elif(choice1==3 and choice2==1 ):
        print ("PLAYER2 WINS")
    elif(choice1==3 and choice2==2 ):
        print ("PLAYER1 WINS")
    else:
        print("....Wrong choice selected....")
else:
    print("...wrong choice.............") 
    



    

