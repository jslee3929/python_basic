# 패키지, 모듈 위치

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
# random 모듈의 파일 위치를 알려줌
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# Travel 폴더 위치를 Lib 폴더 하에 옮겨도 작동 잘 됨.
# 다른 프로젝트를 할 때 이런 식으로 라이브러리를 추가할 수 있음.