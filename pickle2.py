import pickle

menu_file = open("menu_text","rb")
menu=pickle.load(menu_file)
print(menu)
menu_file.close()
