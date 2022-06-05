# 내장함수
# 파이썬에 내장되어 있어 import 없이 바로 사용 가능한 함수

# input : 사용자 입력을 받는 함수
language = input('무슨 언어를 좋아하세요? ')
print('{0}은 아주 좋은 언어입니다.'.format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

import random # random은 외장 함수
print(dir())
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'random']

import pickle
print(dir())
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pickle', 'random']

print(dir(random)) # random 함수 내에서 쓸 수 있는 명령어

lst = [1, 2, 3]
print(dir(lst)) # list 내에서 쓸 수 있는 명령어

name = 'Jim'
print(dir(name))

# 구글에 'list of python builtins' 검색