# 한 줄 for

# 출석번호가 1,2,3,4인 학교가 있었다.
# 그런데 교칙 수정으로 번호 앞에 100을 붙이기로 함. (ex. 101, 102, 103, 104, ...)

students = [1,2,3,4,5]
print(students)

# students 안의 i에 대해 각각 100을 더해주라는 명령
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["아이언맨", "토르", "그루트"]
students = [len(length) for length in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
# 뒤에 .upper를 붙이면 대문자로 변환된다.
students = [i.upper() for i in students]
print(students)