# 리스트 []
# 리스트란 순서를 가진 객체의 집합이다.
# 위의 명령어들을 이용해 내용을 자유롭게 변경 가능함.

# 지하철 칸 별로 10명, 20명, 30명
# 지금까지는 변수별로 숫자를 따로 저장
subway1 = 10
subway2 = 20
subway3 = 30

# 리스트를 사용하면 비슷한 것들을 하나로 묶을 수 있음
subway = [10,20,30]
print(subway)

# 문자로 리스트를 만드는 것도 가능
subway = ["유재석", "조세호", "박명수"]
print(subway) # ['유재석', '조세호', '박명수']

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호")) # 1

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # 가장 뒤에 하하를 넣음.
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # 1번쨰 위치에 정형돈을 넣음.
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

print(subway.pop()) # 꺼내진 사람 이름, 하하
print(subway) # 꺼낸 결과, ['유재석', '정형돈', '조세호', '박명수']

print(subway.pop()) # 박명수
print(subway) # ['유재석', '정형돈', '조세호']

print(subway.pop()) # 조세호
print(subway) # ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway) # ['유재석', '정형돈', '유재석']
print(subway.count("유재석")) # 2

# 정렬하기
num_list = [5,2,4,3,1]
num_list.sort() # 정렬하는 함수
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse() # 순서 뒤집는 함수
print(num_list) # [5, 4, 3, 2, 1]

lst1 = [1, 2, 3, 4, 5]
print('리스트 뒤집기 전 : ', lst1) # [1, 2, 3, 4, 5]
lst2 = reversed(lst1) # 원래 값에는 영향을 미치지 않음.
print('리스트 뒤집은 후 : ', lst1) # [1, 2, 3, 4, 5]

print('리스트3 :', list(lst2)) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear() # 모두 지우는 함수
print(num_list) # []

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1] # 리스트 안에 숫자만 넣을 수도 있지만,
mix_list = ["조세호", 20, True] # 다양한 자료형을 넣을 수도 있음.
print(mix_list)

# 리스트 확장
num_list.extend(mix_list) # num_list와 mix_list를 합침.
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]