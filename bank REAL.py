class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.manager = Manager("John Smith")
        self.customer = Customer("Jane Doe")
        
        def __str__(self) -> str:
            return "This bank name is: " + self.name
       
class Manager:
    def __init__(self, name) -> None:
        self.name = name
        
    def __str__(self) -> str:
        return "Bank Manager: " + self.name
        
class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.account = Account("Saving")
    
    def __str__(self) -> str:
        return "Customer only for: " + self.name
    
class Account:
    def __init__(self, type) -> None:
        self.type = type
        self.balance = 1000
        
    def __str__(self) -> str:
        return "This is a " + self.type + " Account with a " + str(self.balance) 
    
    
    def deposit(self, amount): 
        self.balance += amount
        # self.balance = self.balance + amount
        print(f"Amount ${amount:.2f} has been deposited to the account")
        
    def withdraw(self, amount): 
        self.balance += amount
        # self.balance = self.balance + amount
        print(f"Amount ${amount:.2f} has been withdraw to the account")
        
def let_run():
    bankCBA = Bank("CBA")
    print(bankCBA.customer.account)
    bankCBA = Bank("CBA")
    d_amount = float(input("Amount to deposit $ "))
    bankCBA.customer.account.deposit(d_amount)
    
    print(bankCBA.customer.account)
    w_amount = float(input("Amount to withdraw $ "))
    bankCBA.customer.account.withdraw(w_amount)
 
    
    
    
if __name__ == "__main__":
    let_run()