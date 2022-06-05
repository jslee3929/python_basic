# while

# 스타벅스에서 5번 불렀는데 안 나타나면 커피를 버리는 정책을 만들었다.
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# 무한루프 (강제종료 = Ctrl + C)
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}님, 커피가 준비되었습니다. {1}회 호출했습니다.".format(customer,index))
#     index += 1

# 조건부 반복
# customer = "토르"
# person = "Unknown"

# while person != customer : # person이 customer가 아닐 때 계속 반복
#     print("{0}님, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
#     if person == "토르": # person = customer이므로 반복문 종료.
#         print("맛있게 드세요")
#     else:
#         print("아직 커피가 준비되지 않았습니다.")