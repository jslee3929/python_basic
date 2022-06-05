# __all__
# __init__ 모듈에서 __all__ = ["", ""] 식으로 공개범위를 설정해줘야 읽어올 수 있음.

# from random import *
from travel import * # __init__ 모듈 코드 수정 없이 그냥 돌리면 에러 남.

trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()