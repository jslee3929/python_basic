# 전환값과 반환값

def open_account() : # def + 함수이름() :
    print("새로운 계좌가 생성되었습니다.")

open_account() # 함수를 불러오는 명령

def deposit(balance, money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money # return을 통해 반환된 balance + money를 deposit에 저장.

def withdraw(balance, money): #출금
    if balance >= money: # 잔액이 출금보다 많으면 (출금 가능하면)
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금 (수수료)
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 현재 잔액
balance = deposit(balance, 1000) # 입금 함수 호출, 잔액 + 1000원
balance = withdraw(balance, 2000) # 출금 함수 호출, 출금 불가
balance = withdraw(balance, 500) # 출금 함수 호출, 잔액 - 500원
commission, balance = withdraw_night(balance, 300)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# withdraw_night를 좀 더 규칙성 있게 짜보려고 시도한 건데 실행이 안됨.
# 나중에 똑똑해지면 좀 더 만져볼 예정..

# def open_account() :
#     print('새로운 계좌가 생성되었습니다.')

# open_account()
# balance = 0

# def deposit(balance, money) : # 입금
#     print("{0}원 입금이 완료되었습니다. 잔액은 {1}원 입니다.".format(money, balance + money))
#     return balance + money # return을 통해 반환된 balance + money를 deposit에 저장.

# def withdraw(balance, money): #출금
#     if balance >= money: # 잔액이 출금보다 많으면 (출금 가능하면)
#         print("{0}원 출금이 완료되었습니다. 잔액은 {1}원 입니다.".format(money, balance - money))
#         return balance - money
#     else:
#         print("{0}원 출금을 완료할 수 없습니다. 출금액이 잔액보다 많습니다. 잔액은 {1}원 입니다.".format(money, balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금 (수수료)
#     commission = 100 # 수수료 100원
#     if balance >= money + commission:
#         print("수수료 {0}원을 포함하여 {1}원 출금이 완료되었습니다. 잔액은 {2}원입니다.".format(commission, money, balance - money - commission))
#         return balance - money - commission
#     else:
#         print("{0}원 출금을 완료할 수 없습니다. 수수료를 포함한 출금액이 잔액보다 많습니다. 수수료는 {1}원이며, 잔액은 {2}원 입니다.".format(money, commission, balance)
#         return commission, balance
    

# balance = deposit(balance, 10000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 300)