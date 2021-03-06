# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정.
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가.
# 조건 3 : random 모듈의 shuffle과 sample을 활용.

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # 리스트 셔플하기
# print(lst)
# print(sample(lst, 1)) # 랜덤 숫자 1개 뽑기

# 내 풀이
from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 더러운 버전
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = range(1,21) # 편리한 버전
print(type(lst)) # 그러나 type이 range임. <class 'range'>
lst = list(lst) # type 'range'를 type 'list'로 변환
print(type(lst)) # type이 list로 바뀜. <class 'list'>
shuffle(lst) # 섞어줌

print("-- 당첨자 발표 --")
print("치킨 당첨자 : ", lst.pop()) # 리스트 제일 뒤에서 한 놈 꺼내고 꺼낸 놈 보여줌. 치킨 당첨자 :  11
print(lst) # 한 놈 꺼내고 남은 애들 보여줌. [1, 9, 19, 5, 8, 3, 4, 20, 10, 16, 15, 14, 18, 17, 7, 2, 6, 13, 12]
print("커피 당첨자 : ", sample(lst, 3)) # 리스트에서 무작위로 세 놈 꺼내서 보여줌. 커피 당첨자 :  [8, 16, 20]
print("-- 축하합니다 --")

# 쌤 설명
winners = sample(lst,4) # 당첨자 4명 뽑음
print("치킨 당첨자 : {0}".format(winners[0])) # 1번째 놈 보여줌. 치킨 당첨자 : 18
print("커피 당첨자 : {0}".format(winners[1:])) # 2번째부터 끝놈까지 보여줌. 커피 당첨자 : [14, 4, 17]