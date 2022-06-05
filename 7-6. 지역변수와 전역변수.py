# 지역변수와 전역변수

# 지역변수는 함수 내에서만 쓸 수 있음
# 함수가 호출될 때 만들어지고 함수가 끝날 때 사라진다.
# 전역변수는 프로그램 내에서 어디서나 부를 수 있음.

# 지역변수 선언을 하지 않은 예제 (gun 선언 X)
# gun = 10

# def checkpoint(soldiers): # 경계근무 나가는 군인의 수
#     gun = gun - soldiers # 변수 미설정으로 에러 발생
#     print('[함수 내] 남은 총 : {0}'.format(gun))

# print('전체 총 : {0}'.format(gun))

# checkpoint(2) # 2명이 경계 근무 나감
# print('남은 총 : {0}'.format(gun))

# 함수 내의 지역변수 gun을 사용하는 예제
# gun = 10

# def checkpoint(soldiers):
#     gun = 20
#     gun = gun - soldiers # 지역변수 gun을 사용함.
#     print('[함수 내] 남은 총 : {0}'.format(gun))

# print('전체 총 : {0}'.format(gun))

# checkpoint(2) # 20 - 2 = 18
# print('남은 총 : {0}'.format(gun)) # 함수 외부의 변수를 사용함. 10

# 전역변수를 사용하는 예제
gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))

print('전체 총 : {0}'.format(gun)) # 10
checkpoint(2) # 8
print('남은 총 : {0}'.format(gun)) # 8

# 전역 변수를 너무 많이 쓰면 코드 관리가 어려우므로 권장되는 방법은 아님.

# 권장되는 방법
gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun

print('전체 총 : {0}'.format(gun)) # 10
gun = checkpoint_ret(gun, 2)
print('남은 총 : {0}'.format(gun)) # 8