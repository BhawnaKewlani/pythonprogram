"""Caluculator for  2 no using match """
n1=int(input("Enter 1st Number: "))
n2=int(input("Enter 2nd Number: "))
cal=input("Choose your option (add,sub,mul,div,rem,pow) :")
cal=cal.lower()
match cal:
   case "add": print(n1+n2)
   case "sub": print(n1-n2)
   case "mul": print(n1*n2)
   case "div": print(n1/n2)
   case "rem": print(n1%n2)
   case "pow": print(n1**n2)
   case _:print("Wrong Option")
print("Thanks for coming...........!!!")
