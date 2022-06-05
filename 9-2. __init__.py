# __init__ : 파이썬에서 쓰이는 생성자.
# 마린이나 탱크 같은 객체가 만들어질 때 자동으로 호출됨.
# 클래스로부터 만들어지는 놈들을 객체라고 함.
# 마린과 탱크는 유닛 클래스의 인스턴스.
# 객체가 생성될 때는 기본적으로 init 함수에 생성된 갯수와 동일하게 만들어야 함. (self 제외)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(name)) # self.name을 쓰든 name을 쓰든 상관없음.
        print('체력 {0}, 공격력 {1}'.format(hp, damage))

# marine3 = Unit('마린') # 에러
# marine4 = Unit('마린', 40) # 에러
marine = Unit('마린', 40, 5)