# 표준 입출력

print("Python", "Java") # Python Java
print("Python" + "Java") # PythonJava

print("Python", "Java", sep="") # PythonJava
print("Python", "Java", sep=",") # Python,Java
print("Python", "Java", sep=" ") # Python Java
print("Python", "Java", sep=" vs ") # Python vs Java
print("Python", "Java", "JavaScript", sep=" vs ") # Python vs Java vs JavaScript

# end
# 문장의 끝부분을 end 안의 문자로 바꾸겠다
# end가 없으면 무조건 줄바꿈
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요?

# 표준 출력, 표준 에러
import sys
print('Python', 'Java', file=sys.stdout) # Python Java, stdout = 표준 출력
print('Python', 'Java', file=sys.stderr) # Python Java, stderr = 표준 에러

# 왼쪽, 오른쪽 정렬
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # .items()는 Key와 Value를 쌍으로 가져옴.
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # subject는 총 8칸 공간 확보 후 왼쪽 정렬
    # score는 총 4칸 공간 확보 후 오른쪽 정렬

# 출력 예제
# 수학      :   0
# 영어      :  50
# 코딩      : 100

# 은행 대기순번표
# 001, 002, 003, ...

for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3)) # zfill() = 값이 없는 빈 공간을 0으로 채움.

# 출력 예제
# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# 대기번호 : 004
# 대기번호 : 005

# 표준 입력
answer = input("아무 값이나 입력하세요.")
print('입력하신 값은 ' + answer + '입니다.')
# input으로 들어간 값은 str로 처리됨.
# answer = 10 식으로 변수를 선언하면 그 값은 int임.