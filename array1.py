"""
   시퀸스- 리스트(list) : 순서가 있고,가변(mutable)-ex [1,2,3]
    시퀸스- 튜플(tuple) : 순서가 있고, 불변(immutable)-ex(1,2,3)
    세트- 세트(set) : 순서가 없고, 중복을 허용하지 않음-ex{1,2,3}
    맵- 딕셔너리(dictionary) : 순서가 없고,key/value 쌍으로 이루어짐
    -ex{'a':1,'b:'2','c':3}
    """
hobby = ["축구","골프",333,"농구"]
print(hobby)
print(hobby[0])
hobby.append("수영")
print(hobby)
hobby+=["독서"]
print(hobby)
hobby+=["영화보기","잠자기"]
print(hobby)
hobby.insert(2,"넷플릭스")
print(hobby)
hobby.remove(333)
print(hobby)
hobby.pop()
print(hobby)
del hobby[4]
print(hobby)
del hobby[hobby.index("넷플릭스")]
print(hobby)
print(hobby.count("골프"))
hobby.sort()#오름차순
print(hobby)
hobby.sort(reverse=True)
print(hobby)
hobby.clear()
print(hobby)