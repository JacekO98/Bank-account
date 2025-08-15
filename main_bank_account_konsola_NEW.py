import bank_account
import bankaccount_COM
import pickle

"""Account creation function"""

def create_account(account_list, PLIKZAPISOWY):
    print("Choose account type:")
    print("[S] - Create a standard account")
    print("[C] - Create a company account")

    #User enters initial account data
    accountType = str(input('Select option S or C -->'))
    accountNumber = int(input('Account number:'))
    ownersName = str(input('Username:'))
    accountBalance = float(input('Initial balance:'))

    #Pass these values to the bank_account class to create an object
    if accountType == "S":
        new_account = bank_account.Bank_Account(ownersName, accountNumber, accountBalance, accountType)
    if accountType == "C":
        new_account = bankaccount_COM.Company(ownersName, accountNumber, accountBalance, accountType)

    #Adding a new account to the account list
    account_list.append(new_account)
    savingData(account_list, PLIKZAPISOWY)


"""Money deposit function"""

def deposit(account_list, PLIKZAPISOWY):
    account_number = int(input('Account Number to deposit:'))
    for account in account_list:
        if account.get_id() == account_number:
            depo = float(input('Deposit amount:'))
            account.balance(depo)
            print(f'Sum: {depo} was paid into the account {account_number}')
    savingData(account_list, PLIKZAPISOWY)

"""Money withdrawal function"""

def withdrawn(account_list, PLIKZAPISOWY):
    account_number = int(input('Account Number to withdrawn:'))
    for account in account_list:
        if account.get_id() == account_number:
            wdr = float(input('Withdrawn amount:'))
            account.withdrawn(wdr)

            print(f'Sum: {wdr} was paid into the account {account_number}')
    savingData(account_list, PLIKZAPISOWY)

"""Saving accounts to an external file"""

def savingData(account_list, PLIKZAPISOWY):
    plik = open(PLIKZAPISOWY, 'wb')
    lengh = len(account_list)
    i = 0
    while not i == lengh:
        pickle.dump(account_list[i], plik)
        i = i + 1
    plik.close()

"""Viewing data for all accounts"""
def showAllAccounts(account_list):
    for account in account_list:
        ACNu = account.get_id()
        ACNa = account.get_name()
        ACA = account.get_amount()
        ACT = account.get_type()

        print("********************")
        print(f"Account number: {ACNu}")
        print(f"Owner's name: {ACNa}")
        print(f"Account balance: {ACA}")
        print(f"Account type: {ACT}")

"""Loading data from a file"""

def loadFile(account_list, PLIKZAPISOWY):
    account_list.clear()
    eof = False
    try:
        plik = open(PLIKZAPISOWY, 'rb')
        while not eof:
            try:
                account = pickle.load(plik)
                account_list.append(account)
            except EOFError:
                eof = True
        plik.close()
        print("Accounts from file loaded into list")
    except:
        print("There is no data in the file. You must create an account before uploading!")



"""Main function"""

def main():
    exit_loop = False
    account_list = []

    PLIKZAPISOWY = "plikZapisowy.dat"
    while exit_loop == False:
        # Wyświetlanie Menu
        print("Choose what you want to do:")
        print("[C] - Create an account")
        print("[D] - Deposit money into the account")
        print("[W] - Withdraw money from your account")
        print("[S] - View account information")
        print("[L] - Loading data from a file")
        print("[E] - Exit")

        user_selector = input("Select option C, D, W, S, E or L -->")
        if user_selector == "C":
            create_account(account_list, PLIKZAPISOWY)

        if user_selector == "D":
            deposit(account_list, PLIKZAPISOWY)

        if user_selector == "W":
            withdrawn(account_list, PLIKZAPISOWY)

        if user_selector == "S":
            showAllAccounts(account_list)

        if user_selector == "L":
            loadFile(account_list, PLIKZAPISOWY)

        if user_selector == "E":
            exit_loop = True




if __name__ == "__main__":
    main()













