from random import *

print(random()) # 0.0 이상 1.0 미만의 랜덤 값 생성. (예) 0.09680388729811595
print(random() * 10) # 0.0 이상 10.0 미만의 랜덤 값 생성 (예) 3.571488529137463

# int()는 괄호 안의 수를 정수로 바꿔주는 기능을 함. 
print(int(random() * 10)) # 0 이상 10 미만의 랜덤 정수값 생성 (예) 2
print(int(random() * 10) + 1) # 1 이상 10 이하의 랜덤 정수값 생성 (예) 10

print(int(random())) # 0 이상 1 미만의 랜덤 정수값 생성, 0
print(int(random()) * 45) # 0 이상 45 미만의 랜덤 정수값 생성
print(int(random() * 45) + 1) # 1 이상 45 이하의 랜덤 정수값 생성

# 위 문장을 6번 반복하면 간이 로또 번호 생성기가 된다.
# 숫자를 중복 없이 출력하는 기능이 없으므로 불완전하긴 함.

# randrange와 randint 함수는 정수값을 생성한다.
# 이걸 쓰면 위의 로또 번호 생성기 코드 길이를 좀 더 줄일 수 있음.
# 참고로 from random import * 대신 import random을 쓸 경우
# print(random.randrange)나 print(random.randint)식으로 입력해줘야 한다.
print(randrange(1,46)) # 1 이상 46 미만의 랜덤 정수값 생성
print(randint(1,45)) # 1 이상 45 이하의 랜덤 정수값 생성