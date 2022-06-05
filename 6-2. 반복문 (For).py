# for

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for문 안에서 바로 waiting_no라는 변수를 생성하고 값을 할당.
for waiting_no in [0, 1, 2, 3, 4]: # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

# 아래는 randrange()와 비슷한 용법. 0부터 5 전까지 정수 생성.
for waiting_no in range(5): # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

# range(1, 6)은 1부터 6 직전까지 정수 생성.
for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))

# 리스트를 활용한 예시
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks: # customer라는 변수는 for문 안에서 바로 생성 가능. 따로 생성해 줄 필요가 없다.
    print("{0}, 커피가 준비되었습니다".format(customer))