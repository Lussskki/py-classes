class Bank:
    def __init__(self, money=0, cent=0): 
        self.money = money
        self.cent = cent
    
    def questions(self):
        money = float(input("What money are you using? "))
        return money

def main():
    bank_instance = Bank() 
    money_used = bank_instance.questions()
    print(f"I am using {money_used} american USD")

if __name__ == "__main__":
    main()
