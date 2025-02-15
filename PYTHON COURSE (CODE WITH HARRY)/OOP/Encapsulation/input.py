class BankAccount:
  def __init__(self, account_holder , balance = 0):
    self.__account_holder = account_holder
    self.__balance = balance
  @property
  def balance(self):
    return self.__balance
  
  @balance.setter
  def balance(self, value):
    if isinstance(value , (int, float) and value >= 0):
      self.__balance = value
    else:
      raise ValueError("Balance must be a non_negative number")
    
  def desposit(self, amount):
    if amount > 0:
      self.__balance += amount
    else:
      raise ValueError("Deposit amount must be positive!")
    
  def withdraw(self, amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount
    else:
      raise ValueError("Invalid or insufficient amount")
    
def create_account():
    account_hold = input("Enter the account holder's name: ")
    
    while True:
      try:
        balance = float(input("Enter the Initial Balance: "))
        if balance < 0:
          print("Balance must be a non-negative number.")
        else:
          break
      except ValueError:
        print("Please enter a valid number for balance. ")
    
    account1 = BankAccount(account_hold, balance)
    
    print(f"Account holder: {account_hold}")
    print(f"Initila Balance: {account1.balance}")

    perform_withdrawl(account1)
    
def perform_withdrawl(account1):
  while True:
    while True:
      try:
        amount = float(input("\nEnter the Amount to withdraw: "))
        account1.withdraw(amount)
        print(f"Successfully withdre {amount}. New Balance: {account1.balance}")
        break
      except ValueError as e:
        print(e)
      
create_account()
  