# 메소드
# self는 자기 자신을 의미.
# class 내에서 method의 가장 앞 인자에는 항상 self를 적는다.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # self.name은 전달받은 name 인자를 사용한다.
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

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

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack("5시")

# 공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)

# __init__ : 만들 때 사용하는 메소드.
# attack, damaged : 만든 걸 특정한 방식으로 사용하기 위한 메소드.