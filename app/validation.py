def validate_input(message, options):
    validated_input = None
    while validated_input not in options:
        validated_input = input(message).capitalize()
        if validated_input not in options:
            print("Invalid input. Please, enter one of the available options.")
    return validated_input


def validate_numbers(message,error_message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)

def validate_balance(message,error_message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(error_message)

