# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:57:25 2024

@author: Mantas
"""

'''
Budget and Expense Management System
Greeting.
Introduction to program.
How to use the program
'''
print('Welcome. This is your Budget and Expense helper.')
print('You will set up your budget and will be asked to input your expenses.')
print('It might help you to keep better track of your monthly expenses.')
# Creating empty dictionary and input for user monthly budget.
expenses = {}
budget = float(input("Your monthly Budget: "))
# Predefined categories
categories = {
    "1": "Entertainment",
    "2": "Groceries",
    "3": "Home",
    "4": "Health",
    "5": "Transportation",
    "6": "Others"
}
# Creating the main loop with menu for user's choices and 
# making choice function so user would be able to give input.
while True:
    print("\nMenu:")
    print("1. Your Expense")
    print("2. Edit Expense")
    print("3. Delete Expense")
    print("4. View Budget")
    print("5. Exit")
    choice = input("Choose an option: ")
# Block for input from user.
    if choice == "1":
        print("\nCategories:")
        for key, category in categories.items():
            print(f"{key}. {category}")
        category_choice = input("Choose a category: ")
# Error handling
        try:
            category = categories[category_choice]
            expense_name = input("Name of the expense: ")
        except KeyError:
            print("Invalid input!")
        try:
            expense_amount = float(input("Amount of the expense: "))
        except ValueError:
            print("Please enter a number.")
            continue
# Block to create new entry in dictionary with amount for it
# if one does not exist yet
        if category not in expenses:
            expenses[category] = {}
        expenses[category][expense_name] = expense_amount
        print(f"{expense_name} added to {category} with amount {expense_amount}.")
        total_expenses = sum(sum(category_expenses.values()) for category_expenses in expenses.values())
# Dictionary comprehension to sum up all the values in dictionary.
# message for user about exceeded budget. 
        if sum(expenses[category].values()) > budget:
            print("Your budget is exceeded. Please go back and lower your expense.")
            continue
# Block for editing the entries in dictionary.
    elif choice == "2":
        print("\nCategories:")
        for key, category in categories.items():
            print(f"{key}. {category}")
        category_choice = input("Choose a category: ")
        category = categories[category_choice]
        expense_name = input("Name of the expense: ")
        try:
            expense_amount = float(input("Amount of the expense: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if category in expenses and expense_name in expenses[category]:
# Update the expense amount
            expenses[category][expense_name] = expense_amount
            print(f"{expense_name} updated to {expense_amount}.")
        
# Check if the total expenses exceed the budget
            total_expenses = sum(sum(category_expenses.values()) for category_expenses in expenses.values())
            if total_expenses > budget:
                print("Your budget is exceeded. Please review your expenses.")
        else:
            print("Expense not found. If you want to add, choose option 1.")
# Block for deleting items from dictionary
    elif choice == "3":
        print("\nCategories:")
        for key, category in categories.items():
            print(f"{key}. {category}")
        category_choice = input("Choose a category: ")
        category = categories[category_choice]
        expense_name = input("Name of the expense: ")
        if category in expenses and expense_name in expenses[category]:
            del expenses[category][expense_name]
            print(f"{expense_name} removed from {category}.")
        else:
            print("No such expense.")
# Block for checking the balance and previously entered values for expenses.
    elif choice == "4":
        total_expenses = sum(sum(category_expenses.values()) for category_expenses in expenses.values())
        remaining_budget = budget - total_expenses
        print(f"Remaining budget: {remaining_budget}")
        print("\nExpenses:")
        for category, category_expenses in expenses.items():
            print(f"{category}:")
            for expense, amount in category_expenses.items():
                print(f" {expense}: {amount}")
    
    elif choice == "5":
            break
# Using this else statement if user fails to choose given option from menu.
    else:
        print("Please try again.")

print("Thank you for using the budget management application.")