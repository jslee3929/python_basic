# 사전 (Dictionary)

# 코딩에서 사용하는 사전 자료형은 Key와 Value 형태로 나온다.
# 목욕탕에 가면 Key에 해당하는 사물함(Value)을 열 수 있다.
# 코딩의 Key와 Value도 같은 역할을 한다. 중복된 Key는 존재할 수 없음.

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 에러. 해당하는 key가 없음.
print(cabinet.get(5)) # get을 이용하면 에러가 나는 대신 None이 나옴.
print(cabinet.get(5, "정준하")) # 5 자리에 값이 없으면 "정준하"라는 값을 넣은 후 가져옴.
print("hi")

# 사전 자료형이 있는지 없는지 확인하는 방법
print(3 in cabinet) # True
print(5 in cabinet) # False

# Key에 스트링(문자열)을 지정할 수도 있음.
cabinet = {"A-3":"유재석", "B-100":"김태호"}

print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님이 온 경우.
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국" # A-3에 김종국을 넣겠다. (유재석 삭제)
cabinet["C-20"] = "조세호" # C-20에 조세호를 넣겠다.
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"] # A-3 : 유재석을 삭제
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')]

# cabinet 내용 없애기
cabinet.clear() # cabinet 내용 다 지움.
print(cabinet) # {}