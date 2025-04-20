import re
def validate_input(message, options):
    validated_input = None
    while validated_input not in options:
        validated_input = input(message).upper()
        if validated_input not in options:
            print("Invalid input. Please, enter one of the available options.")
    return validated_input


def validate_numbers(message,error_message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)



def validate_id(message):
    while True:
        try:
            user_input = input(message)  
            if user_input.isdigit():  
                return user_input
            else:
                print("Invalid input. Please, use numbers only.")
        except ValueError:
            print("An unexpected error occurred.")

def validate_email(message):
    while True:
        try:
            user_input = input(message)  
            pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  
            if re.match(pattern, user_input):  
                return user_input
            else:
                print("Invalid input. Please, use a valid email format.")
        except Exception:
            print("An unexpected error occurred.")

