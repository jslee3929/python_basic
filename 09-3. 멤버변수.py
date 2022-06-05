# 멤버변수
# self.name, self.hp, self.damage = 멤버변수.
# 멤버변수 = 클래스 내에서 정의된 변수.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('빼앗은 레이스', 80, 5)
wraith2.clocking = True # 외부에서 클로킹 변수 추가 할당.
# 확장된 변수는 확장한 객체에 대해서만 적용. (wraith2)
# wraith 1에는 적용 안됨.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))