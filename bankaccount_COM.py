
import bank_account
#The bank deposits 10% of the withdrawn value into the account
class Company(bank_account.Bank_Account):
    def withdrawn(self, outcome):
        added_value = 0.1 * outcome
        self.amount += added_value
        print(f"Added to the bill {added_value} the current account balance is {self.amount}")




