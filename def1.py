su=10

def allnew_function():
    print("새 함수지롱")
    
def new_function():
    print("함수지롱")

def su_function(num):
    global su
    num+=10
    su=num
    
def new_su_function(num):
    global su
    num-=5
    su=num
        
new_function()
allnew_function()#매개변수가 없는 함수
new_su_function(su)
print(su)
su_function(su)
print(su)