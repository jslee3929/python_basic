# Super

class Unit: # 부모 class
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, 0)

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

# Super를 쓸 수 없는 경우 예제
class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

# 드랍쉽
dropship = FlyableUnit() # Unit 생성자 (Unit만 상속됨)

class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

# 드랍쉽
dropship = FlyableUnit() # Flyable 생성자 (Flyable만 상속됨)

# 다중 상속시에는 Super를 쓸 수 없음.
class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
# Unit 생성자
# Flyable 생성자
# 위와 같이 하면 둘 다 호출됨.