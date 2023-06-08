import random,datetime
print("Welcome to Radhe Practice Center.")
ques=input("Enter Number of Questions: ")
sTime=datetime.datetime.now()
try:
    ques=int(ques)
except:
    exit()
correct=0
for i in range(0,ques):
    n1=random.randint(-10,50)
    n2=random.randint(-10,50)
    op=random.randint(0,2)
    res=0
    sym=''
    if op==0:
        res=n1+n2
        sym="+"
    elif op==1:
        res=n1-n2
        sym='-'
    elif op==2:
        res=n1*n2
        sym='x'
    answer=input(f"{n1} {sym} {n2} = ")
    if answer==str(res):
        correct+=1
        print('Correct')
    else:
        print("Incorrect")

cTime=datetime.datetime.now()
totalTime=cTime-sTime
t=totalTime.total_seconds()
print(f"Completed in {t} second(s). Correct Answers are {correct} / {ques}. Percentage {correct*100/ques} %.")