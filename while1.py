i=0
while i<10:
    print(i, end=" ")
    i+=1
print() 
x=0
s=0
while True:
    if(x%2==0):
        print(x, end=" ")
        s+=x
    x+=1
    if(s >= 100):
        break
print()
print(s)

