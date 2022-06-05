# 예외처리
# 에러가 났을 때 그에 대해 예외로 처리해주는 것

# ex) 주소에 11층이 적혀있었는데 도착해보니 10층짜리 아파트인 상황
# ex) 버스카드에 잔액이 없는 상황
# ex) 숫자를 입력받는 칸에 문자가 입력된 상황

# try 내부의 문장을 실행하다가 에러가 발생하면 except 내부를 찾음.
# except 내부에 에러를 커버칠 수 있는 문장이 있으면 그 문장을 실행함.

try:
    print('나누기 전용 계산기입니다.')
    num1 = int(input('첫번째 숫자를 입력하세요.'))
    num2 = int(input('두번째 숫자를 입력하세요.'))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))

except ValueError:
    print('에러! 잘못된 값을 입력했습니다.')

except ZeroDivisionError as err:
    print(err) # division by zero

# 뒤에 as ~를 적고 print(~)를 하면 파이썬 기본 에러 문구가 출력됨.

try:
    print('나누기 전용 계산기입니다.')
    nums = []
    nums.append(int(input('첫번째 숫자를 입력하세요.')))
    nums.append(int(input('두번째 숫자를 입력하세요.')))
    # nums.append(int(nums[0] / nums[1])) # IndexError
    print('{0} / {1} = {2}'.format(nums[0], nums[1], int(nums[2])))

except ValueError:
    print('에러! 잘못된 값을 입력했습니다.')

except ZeroDivisionError as err:
    print(err) # division by zero

except Exception as err: # 이외의 모든 에러 처리2
    print(err) # 정확한 에러 메시지 출력

except: # 이외의 모든 에러 처리
print('알 수 없는 에러가 발생하였습니다.')