# 패키지
# 모듈들을 모아놓은 집합
# 하나의 디렉토리에 여러 모듈 파일들을 갖다놓은 것

# 태국과 베트남의 패키지 여행 상품을 제공하는 여행사
import travel.thailand # a.b의 b 자리에는 항상 모듈이나 패키지만 올 수 있음. 클래스/함수는 import 불가능.
# import Travel.Thailand.ThailandPackage # 에러
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from ~ import ~ 구문에서는 모듈/패키지/클래스/함수 모두 import 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam # 모듈 import
trip_to = vietnam.VietnamPackage()
trip_to.detail()