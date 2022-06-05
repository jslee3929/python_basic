# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 승객 50명의 콜을 받을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이 승객의 콜만 받아야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 10분)

# 총 탑승 승객 : 2분

# 내 풀이
# import random

# ride_count = 0

# for passenger in range(1,51):
#     time = random.randrange(5,51)
#     if time <= 15:
#         ride = "O"
#         ride_count += 1
#     else:
#         ride = " "
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(ride, passenger, time))

# print("\n총 탑승 승객 : {0}분".format(ride_count))


# random 관련 애먹었던 사례.
# from random import *를 쓸 때는 random.randrange()라고 안 쓰고 randrange()만 쓴다.
# from random import *

# ride_count = 0

# for passenger in range(1,51):
#     time = randrange(5,51)
#     if time <= 15:
#         ride = "O"
#         ride_count += 1
#     else:
#         ride = " "
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(ride, passenger, time))

# print("\n총 탑승 승객 : {0}분".format(ride_count))

# 쌤 풀이
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1,51): # 승객 (1 ~ 50)
    time = randrange(5, 51) # 소요시간 (5 ~ 50)
    if 5 <= time <= 15: # 소요시간 5~15분 손님 : 매칭 성공/승객 수 증가
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))