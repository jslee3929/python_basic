# 파일 입출력

# 파일 만들고 내용 쓴 후 닫기
score_file = open('score.txt', 'w', encoding='utf8') # w = 덮어쓰기
print('수학 : 0', file=score_file)
print('영어 : 50', file=score_file)
score_file.close()

# 출력 결과 (파일로 저장)
# 수학 : 0
# 영어 : 50

# 파일에 내용 추가하기
score_file = open('score.txt', 'a', encoding='utf8') # a = 내용 추가
score_file.write('과학 : 80')
score_file.write('\n코딩 : 100')
score_file.close()

# 출력 결과 (파일로 저장)
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# 파일의 내용 읽기
score_file = open('score.txt', 'r', encoding='utf8') # r = 내용 읽기
print(score_file.read())
score_file.close()

# 출력 결과
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# 파일의 내용 줄 별로 읽기
score_file = open('score.txt', 'r', encoding='utf8') # r = 내용 읽기
print(score_file.readline()) # 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 출력 결과
# print문은 자동으로 줄바꿈 해줌.
# 수학 : 0

# 영어 : 50

# 과학 : 80

# 코딩 : 100

# print문 자동 줄바꿈 안하고 읽기
score_file = open('score.txt', 'r', encoding='utf8') # r = 내용 읽기
print(score_file.readline(), end="") # 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 출력 결과
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# 파일의 내용이 몇 줄인지 모를 때 readline() 쓰는 방법 (반복문)
score_file = open('score.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line: # 읽을 라인이 없으면
        break    # 반복문 탈출
    print(line)
score_file.close()

# 출력 결과
# 수학 : 0

# 영어 : 50

# 과학 : 80

# 코딩 : 100

# 줄바꿈 안하기
score_file = open('score.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line: # 읽을 라인이 없으면
        break    # 반복문 탈출
    print(line, end='')
score_file.close()

# 출력 결과
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

# 줄 별로 리스트 저장 후 출력
score_file = open('score.txt', 'r', encoding='utf8')
lines = score_file.readlines() # list 형태로 저장
for line in lines: # 리스트에서 1줄씩 불러와 출력
    print(line, end='')
score_file.close()

# 출력 결과
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100