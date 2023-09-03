
for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
        if i==j:
            print()
            break
        
for i in range(1,6):
    for j in range(5,0,-1):
        print("*",end="")           
        if i==j:
            print()
            break

for i in range(1,6):
    for j in range(1,6):
        print(" ",end="")
        if i==j:
            break
    for a in range(5,0,-1):
        print("*",end="")
        if i==a:
            print()
            break      
print()
for i in range(1,6):
    for j in range(5,0,-1):
        print(" ",end="")
        if i==j:
            break
    for a in range(1,6):
        print("*",end="")
        if i==a:
            print("*"*a)
            print()
            break       
for i in range(1,6):
    for j in range(1,6):
        print(" ",end="")
        if i==j:
            break
    for a in range(5,0,-1):
        print("*",end="")
        if i==a:
            print("*"*(6-a))
            print()
            break
print()
for i in range(1,6):
    for j in range(1,6):
        print(" ",end="")
        if i==j:
            break
    for a in range(5,0,-1):
        print("*",end="")
        if i==a:
            print("*"*(6-a))
            print()
            break
for i in range(1,6):
    for j in range(5,0,-1):
        print(" ",end="")
        if i==j:
            break
    for a in range(1,6):
        print("*",end="")
        if i==a:
            print("*"*a)
            print()
            break 
print()           

"""for i in range(1,6):
    for j in range(1,6):
        print(" ",end="")
        if i==a:
            print()
    for a in range(5,0-1)"""
            


