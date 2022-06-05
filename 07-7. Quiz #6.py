# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#     남자 : 키(m) x 키(m) x 22
#     여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.

# 함수 안 쓰고 해결하는 버전
# gender_input = input('성별을 입력하세요. (남/여) : ')
# if gender_input == '남':
#     height_input = input('키를 입력하세요. (cm) : ')
#     std_weight = round(int(height_input) ** 2 * 22 * 0.0001, 2)
#     print('키 {0}cm 남자의 표준 체중은 {1}kg입니다.'.format(height_input, std_weight))
# elif gender_input == '여':
#     height_input = input('키를 입력하세요. (cm) : ')
#     std_weight = round(int(height_input) ** 2 * 21 * 0.0001, 2)
#     print('키 {0}cm 여자의 표준 체중은 {1}kg입니다.'.format(height_input, std_weight))
# else:
#     print('성별을 잘못 입력하셨습니다.')

# 함수 쓰고 해결하는 버전 1
# def std_weight(height, gender):
#     if gender == "남자":
#         weight = round(int(height) ** 2 * 22 * 0.0001, 2)
#         print('키 {0}cm 남자의 표준 체중은 {1}kg입니다.'.format(height, weight))
#     elif gender == "여자":
#         weight = round(int(height) ** 2 * 21 * 0.0001, 2)
#         print('키 {0}cm 여자의 표준 체중은 {1}kg입니다.'.format(height, weight))
#     else:
#         print('잘못 입력하셨습니다.')

# gender = input('성별을 입력하세요 (남자/여자) : ')
# height = input('키를 입력하세요 (cm) : ')
# weight = std_weight(height, gender)

# 함수 쓰고 해결하는 버전 2
# def std_weight(height, gender):
#     if gender == "남자":
#         weight = round(int(height) ** 2 * 22 * 0.0001, 2)
#         return weight
#     elif gender == "여자":
#         weight = round(int(height) ** 2 * 21 * 0.0001, 2)
#         return weight
#     else:
#         print('잘못 입력하셨습니다.')

# gender = input('성별을 입력하세요 (남자/여자) : ')
# height = input('키를 입력하세요 (cm) : ')
# weight = std_weight(height, gender)

# print('키 {0}cm {1}의 표준 체중은 {2}kg입니다.'.format(height, gender, weight))

# 쌤 풀이
# def std_weight(height, gender): # 키 = m단위 (실수), 성별 = '남자' or '여자'
#     if gender == '남자':
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 # cm단위
# gender = '남자'
# weight = round(std_weight(height / 100, gender), 2)
# print('키 {0}cm {1}의 표준 체중은 {2}kg입니다.'.format(height, gender, weight))