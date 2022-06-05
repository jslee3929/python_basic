# 클래스

# # 클래스를 쓰지 않을 경우
# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 체력
# damage = 5 # 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print('체력 {0}, 공격력 {1}\n'.format(hp, damage))

# # 시즈탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드와 시즈 모드가 있음
# tank_name = '시즈탱크'
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))

# # 공격 함수
# def attack(name, location, damage):
#     print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(name, location, damage))

# attack(name, '1시', damage)
# attack(tank_name, '1시', tank_damage)

# # 시즈탱크 추가 생산.
# tank_name2 = '시즈탱크'
# tank_hp2 = 150
# tank_damage2 = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name2))
# print('체력 {0}, 공격력 {1}\n'.format(tank_hp2, tank_damage2))
# attack(tank_name2, '1시', tank_damage2)

# 클래스 = 붕어빵 틀, 틀은 하나, 붕어빵은 무한정.
# 클래스 = 연관이 있는 변수와 함수의 집합.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)