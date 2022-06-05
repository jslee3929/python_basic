# If

# 입력을 문자로 받는 경우
weather = input("오늘 날씨는 어때요? ")    # input = 입력을 받음
if weather == "비" or weather == "눈":    # 만약 조건 1 or 조건 2이면
    print("우산을 챙기세요")               # 조건문 1 실행
elif weather == "미세먼지":               # 만약 조건 3이면
    print("마스크를 챙기세요")             # 조건문 2 실행
else:                                     # 이외의 경우
    print("그냥 나가세요")                 # 조건문 3 실행

# 입력을 숫자로 받는 경우
temp = int(input("기온은 어때요? "))         # 기온은 숫자이기 때문에 int로 감싸줌
if 30 <= temp:                              # 기온이 30도 이상이면
    print("너무 더워요. 나가지 마세요")       # 조건문 실행
elif 10 <= temp and temp < 30:              # 기온이 10~30도 사이이면
    print("괜찮은 날씨에요")                 # 조건문 실행
elif 0 <= temp < 10:                        # and는 바로 써도 됨.
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")