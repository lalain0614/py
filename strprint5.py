str="hello Python is The best in the Language"
print(str.upper())#대문자 변환
print(str.lower())#소문자 변환
print(str.replace("python","java"))#글자 치환
print(len(str))

print(str.count("s")) #특정 문자가 몇번 나오는지를 변환
print(str.find("java"))#index,find 특정 문자의 위치를 검색
print(str.index("best"))#index는 글씨가 없을 떄 오류, find 글씨가 없을 때 -1
print(str.find("best"))#둘 다 대소문자 구분

