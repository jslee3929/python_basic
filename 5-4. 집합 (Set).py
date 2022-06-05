# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # 1, 2, 3. 중복을 허용 안 하기 때문.

java = {"유재석", "김태호", "양세형"} # 기본 선언은 중괄호 {}
python = set(["유재석", "박명수"]) # 리스트[]로 만든 다음 set()으로 감싸줘도 됨.

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) # 교집합 = &, {'유재석'}
print(java.intersection(python)) # intersection도 효과 동일. {'유재석'}

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python) # 합집합 = |, {'박명수', '유재석', '양세형', '김태호'}
print(java.union(python)) # union도 효과 동일. {'박명수', '유재석', '양세형', '김태호'}

# 차집합 (java는 할 줄 알지만 python은 할 줄 모르는 개발자)
print(java - python) # 차집합 = -, {'양세형', '김태호'}
print(java.difference(python)) # difference도 효과 동일. {'양세형', '김태호'}

# python 할 줄 아는 사람이 늘어남
python.add("김태호") # python 세트에 "김태호" 추가.
print(python) # {'유재석', '박명수', '김태호'}

# java를 잊었어요
java.remove("김태호") # java 세트에서 "김태호" 빠짐.
print(java) # {'유재석', '양세형'}