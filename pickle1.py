import pickle
menu_file=open("menu_text","wb")
menu= {"메뉴명":"연포탕","가격":70000,"원산지":["낙지 목포","김치 중국","고추가루 태국"]}
print(menu)
pickle.dump(menu,menu_file)#저장
menu_file.close()


