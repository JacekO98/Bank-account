Description

This is a simple bank account management system that allows creating accounts, making deposits and withdrawals, and viewing account information. The system consists of three main components:
- bank_account.py - Defines the base Bank_Account class with standard banking operations
- bankaccount_COM.py - Defines the Company account class that extends Bank_Account with special features
   main_bank_account_konsola_NEW.py - Main program that handles the user interface and operations

Features
- Create standard or company accounts
- Deposit money into accounts
- Withdraw money from accounts (with special rules for company accounts)
- View all accounts with their details
- Data persistence using pickle serialization
- Company accounts receive 10% bonus on withdrawals

How to Run
- Make sure you have Python installed
- Run the main_bank_account_konsola_NEW.py file
- Follow the menu instructions:

C - Create an account

D - Deposit money

W - Withdraw money

S - View account information

L - Load data from file

E - Exit

Data Storage
- The system stores data in:
- plikZapisowy.dat - Contains all account data

Account Types
Standard Account (S):
- Basic deposit/withdrawal functionality
Company Account (C):
- Receives 10% of withdrawn amount as bonus
- Inherits from Bank_Account class
