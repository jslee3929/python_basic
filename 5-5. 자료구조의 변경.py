# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} # 자료구조 = 세트
print(menu, type(menu)) # {'주스', '커피', '우유'} <class 'set'>

menu = list(menu) # 자료구조를 리스트로 변경
print(menu, type(menu)) # ['주스', '커피', '우유'] <class 'list'>

menu = tuple(menu) # 자료구조를 튜플로 변경
print(menu, type(menu)) # ('주스', '커피', '우유') <class 'tuple'>

menu = set(menu) # 자료구조를 다시 세트로 변경.
print(menu, type(menu)) # {'주스', '커피', '우유'} <class 'set'>