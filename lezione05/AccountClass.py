# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:29:09 2019

@author: Studente
"""

class Account():
    """Simple account class with balance."""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        if self.balance <0:
            raise TypeError('Balance cannot be negative')
        else:
            print('Account created for {}'.format(self.name))
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append('{} deposits {} - {}.'.format(self.name,amount,1))
    
    def withdraw(self, amount):
        if amount > 0.:
            if (self.balance - amount) > 0:
                self.balance -= amount
                self.transactions.append('{} withdrows {} - {}.'.format(self.name, amount, 1))
                
    def show_balance(self):
        print('Your balance is {}'.format(self.balance))
        print(self.transactions)

if __name__ == '__main__':
    account_instance = Account('Nicola', 1000)
    account_instance.deposit(200)
    account_instance.show_balance()
    account_instance.withdraw(450)
    account_instance.show_balance()
