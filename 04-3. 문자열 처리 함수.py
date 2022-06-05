# 문자열 처리 함수

python = 'Python is Amazing'
print(python.lower()) # 소문자로 변환. python is amazing
print(python.upper()) # 대문자로 변환. PYTHON IS AMAZING
print(python[0].isupper()) # n번째 문자가 대문자인지 확인. True
print(python[0].islower()) # n번째 문자가 소문자인지 확인. False
print(len(python)) # 문자열의 길이 출력. 17
print(python.replace('Python', 'Java')) # 원하는 문자열 교체. Java is Amazing

# 처음으로 나오는 특정 문자 찾기
index = python.index("n")
print(index) # 5

# 두번째로 나오는 특정 문자 찾기
index = python.index("n", index + 1) # 쉼표 뒤는 시작 위치.
# 처음으로 나오는 위치 = 5
# index + 1 = 5 + 1 = 6번째 자리부터 찾음.
print(index) # 15

# index와 find의 차이
print(python.find('n')) # 5
# index와 동일하게 작동.
print(python.find('java')) # -1
# find는 찾는 문자열이 없을 경우 -1을 반환.
print(python.index('Java')) # Error
# index는 찾는 문자열이 없을 경우 오류가 남.

# 문자열 갯수 세기
print(python.count('n')) # 2