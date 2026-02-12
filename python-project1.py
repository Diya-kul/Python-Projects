# importing necessary python modules
import json     #to store data in json file
import csv
from datetime import datetime as dt
import os   # fro data handling

FILE_NAME = "expensefile.json"

class expenseTracker:
    
    # when object is created, it run automatically. __init__ is a python constructor
    def __init__(self):
        self.expenses = []      # every object of expense tracker will have its own expence list.
        self.load_data()        # program state is restored when object is created. 
        
    #-----------data handling----------------------
    
    #function loads previously saved expenses from json file into memory
    def load_data(self):
        
        # if file exists then read data
        if os.path.exists(FILE_NAME):      
            with open(FILE_NAME, "r") as file:
                self.expenses = json.load(file)
        
        # else start fresh      
        else:
            self.expenses = []
            
    # function save or writes data into json file to save data permanently
    def save_data(self):
        with open (FILE_NAME, "w") as file:
            json.dump( self.expenses, file, indent=4)       # convert python data to json fromate
            
    # with automatically closed the file
    
    #--------1. Add expense------------------------------
    
    # function add expense
    def add_expenses(self):
        # error handling
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            note = input("Enter note: ")
            
            # validate date formate
            dt.strptime(date, "%Y-%m-%d" )
            
            # creating expense dictionary
            expense = {
                "id" : len( self.expenses ) +1,
                "amount" : amount,
                "category" : category,
                "date" : date,
                "note" : note
                
            }
            
            # add new expense into memory list, this only update in RAM
            self.expenses.append(expense)
            self.save_data()        # this update list to json file
            print(" Expense added successfully! ")
            
        except ValueError:
            print("\n\n          Invalid input. Please check amount/date format.")
            
    
    #-------------2. view expense------------------------------------
    def view_expenses(self):
        if not self.expenses:
            print("\n\n No expense found. ")
            return
        
        print("\n-------All Expenses---------")
        for exp in self.expenses:
            print( f''' \n\nID: { exp['id'] } | spend: { exp['amount'] } on { exp ['category'] } at { exp['date']} "{exp['note']}"''')
                  
    #-----------3. Delete Expense-----------------------------------
    def delete_expenses(self):
        try:
            exp_id = int(input("Enter Expense ID to detete: "))
            self.expenses = [exp for exp in self.expenses if exp["id"] != exp_id]
            self.save_data()
            print("Expense delete successfully! ")
            
        except ValueError:
            print(" Invalid ID!")
        
    #------------4. Monthly summary--------------------------------
    def monthly_expenses(self):
        month = input("Enter month (YYYY-MM): ")
        total =0
        
        for exp in self.expenses:
            if exp["date"].startswith(month):
                total += exp["amount"]
                
        maxExpense= max(self.expenses("amount"), maxExpense)
        print(maxExpense)
                
        print(f'''\n\n Total Expenses for {month}:"{total}"''')
        
    #------------5. Filter by Category-----------------------------
    def filter_by_category(self):
        category = input("Enter category to filter: ").lower()
        
        filtered = [ exp for exp in self.expenses if exp["category"].lower() == category]
        
        if not filtered:
            print("\n\n No expenses found for this category. ")
            return
        
        print("\n-------Filtered Expenses--------")
        for exp in filtered:
            print( f'''\n\n ID: { exp['id'] } | spend: { exp['amount'] } on { exp ['category'] } at { exp['date']} "{exp['note']}"''')
            
    #-------------6. Export to csv file-----------------------------
    def export_to_csv(self):
        file_name = "expense_report.csv"
        
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            
        for exp in self.expeses:
            writer.writerow( f''' ID: { exp['id'] } | spend: { exp['amount'] } on { exp ['category'] } at { exp['date']} "{exp['note']}"''')
            
        print(f"\n\n Data exported to {file_name}")
        
        
#---------------------CODE START FROM HERE--------------------------

def main():
    track = expenseTracker()
    
    while True:
        print("\n----------------Expense Tracker----------------")
        print(" 1. Add Expense")
        print(" 2. View Expense")
        print(" 3. Delete Expense")
        print(" 4. Monthly Expense")
        print(" 5. Filter by Category")
        print(" 6. Export to CSV")
        print(" 7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            track.add_expenses()
        elif choice == "2":
            track.view_expenses()
        elif choice == "3":
            track.delete_expenses()
        elif choice == "4":
            track.monthly_expenses()
        elif choice == "5":
            track.filter_by_category()
        elif choice == "6":
            track.export_to_csv()
        elif choice == "7":
            print(" Exiting...  Goodbye!    ")
        else:
            print(" Invalid choice. Try again. ")
            
#--------calling of main function------------
if __name__ == "__main__":
    main()