
import json
from app.validation import validate_input
from app.register_log import *
from app.bank_manager import *

customer_data_file = "data/datos.json"

try:
    with open(customer_data_file, 'r') as file:
        customer_data = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{customer_data_file}' is not found.")
    customer_data = {}
except json.JSONDecodeError:
    print(f"Error: The file '{customer_data_file}' contains invalid JSON data.")
    customer_data = {}
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
    customer_data = {}


def save_customers(customers, customer_data_file):
    with open(customer_data_file, "w") as f:
        json.dump(customers, f, indent=4)

def introduction():
    print("\nHello user, this is a bank account simulator")
    print("\nPlease choose an option of the following: ")

def bank_account_introduction():
    print("Your options are the following: ")
    print("""
        1. Check balance
        2. Deposit
        3. Withdraw
        4. View history
        5. Log out
            """)
    
def bank_account_functions(user_id, customer_data):
    user_data = customer_data[user_id]
    account = BankAccount(user_id, user_data)

    while True:
        bank_account_introduction()
        option = validate_input("Choose one: ", ["1", "2", "3", "4", "5"])

        if option == "1":
            account.check_balance()
        elif option == "2":
            amount = float(validate_numbers("Enter deposit amount: ", "Invalid amount."))
            account.deposit(amount)
            print("Deposit successful.")
        elif option == "3":
            amount = float(validate_numbers("Enter withdrawal amount: ", "Invalid amount."))
            account.withdraw(amount)
        elif option == "4":
            account.view_history()
        elif option == "5":
            customer_data[user_id] = account.export_data()
            save_customers(customer_data, customer_data_file)
            print("Logging out...")
            break


def main():
    while True:
        introduction()
        print("\nWhat do you want to do?")
        print("""
            1. Register
            2. Log in
            3. Exit
        """)

        user_choice = validate_input("Choose one of the available options: ", ["1", "2", "3"])

        if user_choice == "1":
            added = user_register(customer_data)
            if added is None:
                print("The ID was already in the database.")
                continue

            try:
                save_customers(added, customer_data_file)
            except Exception as e:
                print(f"An unexpected error occurred while writing to the file: {e}")
                continue

            print("\nThank you! Your account has been successfully registered.\n")
            print("\nTo access the bank functions please log in")
            print("\n")
            print("\n")

        elif user_choice == "2":
            logged_in = user_log_in(customer_data)
            if logged_in is None:
                print("The ID wasn't found in the database.")
                continue

            print("You logged in successfully!")
            bank_account_functions(logged_in, customer_data)

        elif user_choice == "3":
            print("Thank you for using the Bank Account Simulator. Goodbye!")
            break


main()