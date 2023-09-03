num=[1,2,3,4,5,6,7,8,9,10]
print(num)

num_for = [i*10 for i in num]
print(num_for)

su=[x for x in range(0,100,2)]
print("짝수 :",end=" ")
print(su)

city =["Seoul","Newyork","Paris","Mexico","LA"]
print(city)
city_len = [len(i) for i in city]
print(city_len)
city_swap=[i.swapcase() for i in city]#swapcase()는 글자를 반대로 바꿔버림(대문자->소문자,소문자->대문자)
print(city_swap)

