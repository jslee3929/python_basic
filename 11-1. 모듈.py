# 모듈

# 소프트웨어도 타이어나 범퍼처럼 부품만 교체하거나 추가할 수 있도록 만들면 유지보수가 쉽고 코드의 재사용도 쉬움
# 부품처럼 프로그래밍 하는 것을 모듈화라고 함
# 파이썬에서는 함수 정의나 클래스 등의 코드를 담고 있는 파일을 모듈이라고 함
# 모듈의 확장자는 .py임

# 현금만 받는 극장
# 잔돈을 바꿔주지 않음
# 사람 수에 따라 가격이 얼마인지 알 수 있는 모듈

import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조할인 영화 보러 갔을 때 가격
theater_module.price_soldier(5) # 군인 5명이서 영화 보러 갔을 때 가격

import theater_module as mv # theater_module에 별명을 붙여줌. (mv로 theater_module 호출)
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # from random import *과 같은 용법. 바로 함수 쓰면 됨.
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 특정 함수만 가져다 쓰기
price(5)
price_morning(6)
# price_soldier(4) # 에러

from theater_module import price_soldier as price # price_soldier의 별명을 price라고 할 수 있음.
price(5) # 5명의 군인 할인 가격은 20000원입니다.