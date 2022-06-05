# 상속 : 겹치는 내용을 물려받는다.

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # Unit을 상속.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속 내용
        self.damage = damage # damage만 추가 정의

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))
        # self.name과 self.damage는 __init__ 함수에서 받은 내용을 사용.
        # location은 attack 함수에서 받은 내용을 사용.
    
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack("5시")

# 공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)

# 같은 함수 안에서 사용할 때는 self.name과 name 중 아무거나 써도 됨
# 다른 함수 안에서 사용할 때는 self.name을 써야 함