import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

class FinanceTracker:
    def __init__(self):
        #initialization of data frame to store transactions
        self.transactions = pd.DataFrame(columns=["Date","Description","Category","Amount","Type"])

    def add_transaction(self,description,category,amount,type="Expense"):
        # new transaction is updated here

        transaction={
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Description":description,
            "Category": category,
            "Amount": amount,
            "Type": type
        }

        self.transactions = pd.concat([self.transactions, pd.DataFrame([transaction])],ignore_index = True)
    
    def enter_transactions(self):
        while True:
            print("\n Enter Transaction Details: ")
            description = input("Description: ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            type = input("Type (Income or Expense): ").capitalize()

            #add trasaction
            self.add_transaction(description,category,amount,type)

            # ask if any other entries
            cont = input(" Would you like to add another transaction?   (YES / NO):").upper()
            if cont != "YES":
                break


    
    def save_to_csv(self,filename="transaction.csv"):
        #transactions saved to csv file
        self.transactions.to_csv(filename, index=False)

    def load_from_csv(self, filename="transaction.csv"):
        # loading trasaction  from csv
        self.transactions = pd.read_csv(filename)

    def view_summary(self):
        #displays income, expense and balance
        income = self.transactions[self.transactions["Type"]=="Income"]["Amount"].sum()
        expense = self.transactions[self.transactions["Type"]=="Expense"]["Amount"].sum()
        balance = income - expense
        print(f"Total Income : Rs.{income: .2f}")
        print (f"Total Expenses : Rs.{expense: .2f}")
        print(f"Current Balance: Rs.{balance: .2f}")
    
    def visualize_expenses(self):
        # visualization of expenses is shown by means of a piechart by diving categories
        
        expenses = self.transactions[self.transactions["Type"]=="Expense"]
        category_expenses = expenses.groupby("Category")["Amount"].sum()

        plt.figure(figsize = (8,6))
        category_expenses.plot.pie(autopct='%1.1f%%')
        plt.title("Category based Expenses")
        plt.ylabel('')
        plt.show()


""" Add and View Transactions """

#initialization of tracker
tracker = FinanceTracker()

# enter transactions
tracker.enter_transactions()

#view summary
tracker.view_summary()

#visualize expenses
tracker.visualize_expenses()

#save the transaction to csv
tracker.save_to_csv()
