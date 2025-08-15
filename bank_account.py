# Creating a Bank Account class containing deposit and withdrawal methods,
# Listing all accounts along with information about them, etc.

class Bank_Account:
    def __init__(self, name, ID, initial_amount, account_type):
        self.name = name
        self.ID = ID
        self.amount = initial_amount
        self.account_type = account_type

# Deposit of specified funds
    def balance(self, income):
        self.amount += income
        print(f"The account balance is {self.amount}")


# Withdrawal of specified funds

    def withdrawn(self, outcome):
        if outcome <= self.amount:
            self.amount = self.amount - outcome
        else:
            print("You do not have sufficient funds in your account")

# View account information

    def print_informations(self):
        print(self.name, self.ID, self.amount)

# Deleting the account after selecting the checkout

    def delete_account(self, account_list, ID):
        self.zero_balance = self.amount
        self.withdrawn(self.zero_balance)
        for ID in account_list:
            account_list.pop(ID)
            print(f"Sum {self.zero_balance}, has been selected. Account number {self.ID} has been deleted")

# Receiving Account Details
    def get_name(self):
        return self.name

    def get_id(self):
        return(self.ID)

    def get_amount(self):
        return(self.amount)

    def get_type(self):
        return(self.account_type)











