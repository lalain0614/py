city={"seoul","kangwon","deajeon","changwon","incheon","jeju"}
print(city)
city.add("suwon")
print(city)

print("boundang"in city)
print("seoul"in city)

city.remove("jeju")
print(city)

city2={"seoul","deajeon","inchean","deagu","yangyang"}

print(city|city2)
print(city.union(city2))#합집합

print(city-city2)
print(city.difference(city2))#차집합

print(city^city2)
print(city.symmetric_difference(city2))#대칭차집합

print(city&city2)
print(city.intersection(city2))#교집합

