class BankAmerica:
    accounts = []

    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAmerica.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount 
        print(self.balance)
        return self   

    def display_account(self):
        return f"{self.balance}"

    
    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("insufficient funds:Charging fee=$10.00")
        else:
            self.balance -= amount
        print("The remaining balance is:", self.balance)
        return self

class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAmerica(.02,1089900),
            "savings" : BankAmerica(.02,309000)
        }
        
    def display_account_info(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account()}")
        return self


logan = User("Logan")

logan.account['checking'].deposit(200)
logan.account['savings'].deposit(3444).withdraw(80000)
logan.display_account_info()

nick = User("Nick")
nick.account['checking'].deposit(39000).deposit(380).withdraw(390000)
nick.account['savings'].deposit(700)
nick.display_account_info()        

