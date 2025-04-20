from app.validation import *

def user_register(customer_data):
    user_id = validate_id("What's your id? (Numbers Only): ")
    if user_id in customer_data:
        print(f"The ID {user_id} is already registered.")
        return None
    
    user_name = input("What's your name?: ").capitalize()
    user_email = validate_email("What's your email?: ")
    print("\nNow, I need you to give your bank account data.")

    bank_account_id = validate_numbers("What's your bank account id? (Numbers Only): ","Invalid bank account id, please enter numbers only.")
    account_balance = float(validate_numbers("What's your bank account balance? (Numbers Only): ","Invalid bank account balance, please enter numbers only."))
    
    print("\nThe currencies that are available are: ")
    print("""
        1. USD
        2. ARS
        3. EUR
        4. JPY\n""")

    currency = validate_input("What's the currency of the account?: ",["USD","ARS","EUR","JPY"])

    customer_data[user_id] = {
        "name": user_name,
        "id": user_id,
        "email": user_email,
        "bank_account": {
            "account_id": bank_account_id,
            "account_balance": account_balance,
            "currency": currency,
            "transactions_history": []
        }
    }
    return customer_data

def user_log_in(customer_data):
    user_id = input("What's your id? (Numbers Only): ")
    if user_id in customer_data:
        return user_id
    else:
        print(f"The ID {user_id} is not in the database")
        return None

