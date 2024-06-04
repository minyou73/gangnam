## **문제: 은행 관리 프로그램**

# 1. `Account` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행 계좌의 소유주 이름과 초기 잔액을 설정합니다.
#     - `deposit` 메서드를 사용하여 입금을 처리합니다.
#     - `withdraw` 메서드를 사용하여 출금을 처리합니다. 출금할 금액이 잔액보다 크면 출금을 허용하지 않습니다.
#     - `display_balance` 메서드를 사용하여 현재 잔액을 출력합니다.
# 2. `Bank` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행의 이름을 설정합니다.
#     - `create_account` 메서드를 사용하여 새로운 계좌를 생성합니다.
#     - `get_account` 메서드를 사용하여 계좌를 반환합니다.
#     - `display_accounts` 메서드를 사용하여 현재 은행에 있는 모든 계좌 정보를 출력합니다.
# 3. 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하세요.
# 사용자가 프로그램을 종료하고 싶을 때에는 "종료"를 입력하면 됩니다.


class Account:

    def __init__(self, owner, money=0):
        self.owner = owner
        self.money = money
    
    def deposit(self, amount): #입금
        money += amount
  
    def withdraw(self, amount): #출금
        money -= amount
        if amount > money:


   def display_balance(self):

class Bank:
    
    def __init__(self, name):
        self.name = name
        self.accounts= []

    def create_account(self, owner, money=0):
        account = Account(owner, money)
        self.accounts.append(account)
        print(f'{owner}님의 계좌가 생성되었습니다')

#     def get_account(self, owner):
        for i in self.accounts:
            if i.owner == owner:
                return account
            
#     def display_accounts:

def Main():
    bank = Bank()
    while True:
        print("1. 계좌생성")
        print("2. 입금")
        print("3. 출금")
        print("4. 잔액조회")
        print("5. 종료")

        a = input()
        if a == '1':
            owner = input('소유주의 이름을 입력하세요:')
            bank.create_account(owner)

        elif a == '2':
            owner = input('소유주 이름을 입력하세요:')
            account= bank.get_account(owner)
            
        elif a == '3':
          
        elif a == '4':
            cmd = input('조회할 계좌명 이름').split()
            if len(cmd) == 1:
                number =cmd[0]
                bank.get_account(number)

    
