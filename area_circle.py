# pi*r*r;
r=input("Enter the radius: ")
try:
    r=int(r)
except:
    print("Please enter a number")
    exit()
pi=3.14
a=pi*r**2  #for r square 
print(f"Area of circle is : {a}")
