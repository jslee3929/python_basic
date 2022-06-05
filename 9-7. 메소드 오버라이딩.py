# 메소드 오버라이딩
# 자식 클래스에서 정의한 메소드를 사용하고 싶을 때, 메소드를 새롭게 정의해서 사용할 수 있음.
# 이를 메소드 오버라이딩이라고 함.

# 일반 유닛
class Unit: # 부모 class
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 자식 class
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속 내용
        self.damage = damage # damage만 추가 정의

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))
            
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송. 공격 불가

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # class 2개 상속.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0, 메소드 오버라이딩
        Flyable.__init__(self, flying_speed) # 메소드 오버라이딩

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location) # move 메소드는 Unit 클래스에도 존재하지만, FlyableAttackUnit의 메소드가 우선하여 적용됨 (오버라이드)

# 벌쳐 : 지상 유닛, 기동성이 좋음.
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 아래와 같이 하면 지상 유닛은 move 함수 쓰고, 공중 유닛은 Fly 함수 써야 해서 귀찮음.
vulture.move('11시')
battlecruiser.fly(battlecruiser.name, '9시')

# 메소드 오버라이딩을 통해 똑같은 move 함수를 사용해서 이동 명령을 내릴 수 있음.
battlecruiser.move('9시')