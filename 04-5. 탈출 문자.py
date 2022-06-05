# 탈출 문자

# \n : 줄바꿈
print('백문이 불여일견\n백견이 불여일타')
# 백문이 불여일견
# 백견이 불여일타

# \', \" : 따옴표를 문자로 처리
print("저는 \"나도코딩\"입니다.")
print('저는 \'나도코딩\'입니다.')

# \\ : \를 2번 쓰면 문장 내에서는 \ 1번으로 바뀜.
# print('C:\Users\User\Desktop\PythonWorkspace') # 오류 발생
print('C:\\Users\\User\\Desktop\\PythonWorkspace') # \\이 \로 출력됨.

# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine') # PineApple
# 'Red Apple'을 적은 후 커서가 앞으로 이동해서 'Pine'을 적음.

# \b : 백스페이스 (한 글자 삭제)
print("Redd\b Apple") # Red Apple
# 잘못 입력된 'd'를 지움.

# \t : 탭 (Tab)
print('Red\tApple') # Red   Apple