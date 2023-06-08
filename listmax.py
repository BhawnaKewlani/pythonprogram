lt=[]
n=int(input("Enter the no till u wanted to enter : "))
for i in range(0,n):
    x=int(input(f"enter val{i+1} at : "))
    lt.append(x)
print(max(lt))
#print(sum(lt))
'''lt.sort()
print(lt)'''
print(sorted(lt))
