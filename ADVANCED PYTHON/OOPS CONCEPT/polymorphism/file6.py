#Class - Bank
#method1 - account creation
       #arguments- [ name,a/c number,minimum_balance]
#method2 - withdraw
       #argument - [w_amount]
#method3 - deposit
       #argument - [d_amount]

class Bank:
    Bankname="Federal"


    def account(self,name,account):
       self.name=name
       self.account=account
       self.min_bal=1000
       self.balance=self.min_bal

    def deposit(self,d_amount,):
        self.d_amount=d_amount
        self.balance=self.balance+self.d_amount
        print("your",Bank.Bankname,"account has been credited with",self.d_amount)
        print("Total", Bank.Bankname, " bank balance is", self.balance)

    def withdraw(self,w_amount):
        self.w_amount=w_amount
        if(self.w_amount>self.balance):
            print("insufficient balance")
        else:
            self.balance=self.balance-self.w_amount
            print("your",Bank.Bankname,"account has been debited by",self.w_amount)
            print("Total",Bank.Bankname,"bank balance is",self.balance)

ob=Bank()
ob.account("arun",1234)
ob.deposit(3000)
ob.withdraw(1500)