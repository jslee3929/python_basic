# 사용자 정의 예외처리
# 에러를 직접 정의할 수 있음.

class BigNumberError(Exception): # 에러의 이름 정의
    pass

try:
    print('한 자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10: # 두 자리 수 이상
        raise BigNumberError # 에러 발생시키기 (BigNumberError)
    print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))

except ValueError:
    print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')

except BigNumberError:
    print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')

# 에러와 함께 메시지 출력
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print('한 자리 숫자 나누기 전용 계산기')
#     num1 = int(input('첫 번째 숫자를 입력하세요 : '))
#     num2 = int(input('두 번째 숫자를 입력하세요 : '))
#     if num1 >= 10 or num2 >= 10: # 두 자리 수 이상
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 에러 발생시키기 (BigNumberError)
#     print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))

# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')

# except BigNumberError as err:
#     print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
#     print(err)