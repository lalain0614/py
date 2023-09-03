pororo={1:'뽀로로',2:"루피",3:'크롱',4:'포비'}

print(pororo)
print(pororo[4])
print(pororo.get(2))
print(pororo.get(6))
print(pororo.get(6,"에디"))

pokemon={"AA01":"뮤츠","BB02":"리자몽","CC03":"피카츄"}
print(pokemon["CC03"])
print(pokemon.get("AA01"))
pokemon.update({"DD04":"뮤"})
print(pokemon)
print(pokemon.keys())
print(pokemon.values())
print(pokemon.items())

del pokemon["CC03"]
print(pokemon)

onpiece={"선장":"루피","부선장":"조로","의사":"트리팔가로우","의사":"쵸파"}
print(onpiece)

pororo_animal={1:["뽀로로","펭귄"],2:["루피","비비"],3:["크롱","공룡"]}
print(pororo_animal)
print(pororo_animal[3])
print(pororo_animal[3][1])
pororo_animal[3].append("최애")
print(pororo_animal)

del pororo_animal[3][pororo_animal[3].index("공룡")]
print(pororo_animal)

