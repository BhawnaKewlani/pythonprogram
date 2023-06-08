name= input("Enter Name:")
exp= input ("Enter Experience in Year:")
exp=int(exp)
salary=input("Enter Last Year Salary:")
salary=int(salary)
if(exp>3):
    salary=salary+(salary*5)/100
    print("Dear",name ,",your salary is",salary)    
else:
    print("Dear",name ,",your salary is",salary)