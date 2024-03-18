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
        self.account = Account("Saving", 1000)
    
    def __str__(self) -> str:
        return "Customer only for: " + self.name
    
class Account:
    def __init__(self, type, balance) -> None:
        self.type = type
        self.balance = balance
        
    def __str__(self) -> str:
        return "This is a " + self.type + " Account with a " + str(self.balance) 
    
    
    def deposit(self, amount): 
        self.balance += amount
        # self.balance = self.balance + amount
        print(f"Amount deposited: ${amount:.2f}")
        
    def withdraw(self, amount): 
        if self.balance >= amount:
        
            self.balance = self.balance - amount
            print(f"Amount withdrawn: ${amount:.2f}")
        else:
            print(f"Insufficient fund")
        
    def showBalance(self): 
        print(f"Starting balance: ${self.balance:.2f}")
        
    
if __name__ == "__main__":
    bankCBA = Bank("CBA")
    choice = input("Start banking (d/w/s/x)")
    while choice != "x":
        match choice:
            case 'd':
                d_amount = float(input("Amount to deposit $ "))
                bankCBA.customer.account.deposit(d_amount)
            case 'w':
                w_amount = float(input("Amount to withdraw $ "))
                bankCBA.customer.account.withdraw(w_amount)
            case's':
                bankCBA.customer.account.showBalance()
            case _:
                print("Please type 'd', 'w','s' or 'x' to exit")
        choice = input("Continue banking (d/w/s/x)")
            
    
    print("End of banking, good bye!")
        
    #let_run()
    
    #def let_run():
    #bankCBA = Bank("CBA")
    #print(bankCBA.customer.account)
    #bankCBA = Bank("CBA")
    #d_amount = float(input("Amount to deposit $ "))
    #bankCBA.customer.account.deposit(d_amount)
    
    #print(bankCBA.customer.account)
    #w_amount = float(input("Amount to withdraw $ "))
   # bankCBA.customer.account.withdraw(w_amount)