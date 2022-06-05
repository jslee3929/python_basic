# 연산자

print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 제곱, 2^3 = 8
print(5%3) # 나머지 구하기 = 2
print(10%3) # 1
print(5//3) # 몫 구하기 = 1
print(10//3) # 3

print(10 > 3) # 초과, True
print(4 >= 7) # 이상, False
print(10 < 3) # 미만, False
print(5 <= 5) # 이하, True

print(3 == 3) # 같다, True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # 같지 않다, True
print(not (1 != 3)) # '같지 않다'의 반대 상태, False

print((3 > 0) and (3 < 5)) # 두 조건을 동시에 만족하는지 여부, True
print((3 > 0) & (3 < 5)) # and 대신 &도 쓸 수 있음

print((3 > 0) or (3 > 5)) # 두 조건 중 하나를 만족하는지 여부, True
print((3 > 0) | (3 > 5)) # or 대신 |도 쓸 수 있음

print(5 > 4 > 3) # 여러 연산자를 한 번에 쓸 수 있음, True
print(5 > 4 > 7) # False