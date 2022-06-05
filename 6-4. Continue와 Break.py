# Continue와 Break

# continue를 사용하면 if 뒤의 조건이 True일 경우 print를 실행시키지 않고 다음 반복으로 넘어간다.
# 아래 예제에서는 2번과 5번이 결석이므로 2번과 5번은 실행을 안 하게 됨.
# 반복문 실행 중 Break를 만나면 뒤의 반복을 무시하고 반복문을 종료함.

absent = [2, 5] # 결석한 번호
nobook = [7] # 책을 깜빡하고 안 가져옴

for student in range(1,11): # 출석번호 1번 ~ 10번
    if student in absent:
        continue # 2, 5번 차례에서는 print를 실행 안 시키고 다음 번호로 넘어감.
    elif student in nobook:
        print("오늘 수업은 여기까지. {0}번은 교무실로 따라와".format(student))
        break
    print("{0}번, 책을 읽어보세요.".format(student))