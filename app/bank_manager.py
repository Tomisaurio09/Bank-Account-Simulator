#Esta es una lista de metodos/acciones que puede tomar el usuario solo cuando ya se registro
import datetime

class BankAccount:
    def __init__(self,user_id, user_data):
        self.user_id = user_id
        self.name = user_data["name"]
        self.email = user_data["email"]
        self.bank_account_id = user_data["bank_account"]["account_id"]
        self.balance = float(user_data["bank_account"]["account_balance"])
        self.currency = user_data["bank_account"]["currency"]
        self.history = user_data["bank_account"]["transactions_history"]

    def check_balance(self):
        print(f"Your current balance is {self.balance}")
    
    def deposit(self,amount):
        if amount <= 0:
            print("The amount to deposit must be greater than 0")
            return
        self.balance += amount
        self.add_movement("Deposit",amount)
        self.check_balance()
    
    def withdraw(self,amount):
        if amount <= 0:
            print("The amount to withdraw must be greater than 0")
            return
        if amount > self.balance:
            print("Not enough founds")
            return
        self.balance -= amount
        self.add_movement("Withdraw",amount)
        self.check_balance()

    def view_history(self):
        if not self.history:
            print("No transactions available.")
            return
        
        for movement in self.history:
            print(f"""
                    Type: {movement["type"]},
                    Amount: {movement["amount"]},
                    Date: {movement["datetime"]}
                    """)
        
    def add_movement(self,type,amount):
        movement = {"type": type,"amount": amount, "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        self.history.append(movement)

    def export_data(self):
        return {
            "name": self.name,
            "id": self.user_id,
            "email": self.email,
            "bank_account": {
                "bank_account_id": self.bank_account_id,
                "account_balance": self.balance,
                "currency": self.currency,
                "transactions_history": self.history
            }
        }