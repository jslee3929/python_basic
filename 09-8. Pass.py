# Pass
# 아무것도 안하고 넘어간다. 완성된 것처럼 넘어감.

class Unit: # 부모 class
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, '7시')

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()