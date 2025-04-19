def validate_input(message, options):
    validated_task = None
    while validated_task not in options:
        validated_task = input(message).capitalize()
        if validated_task not in options:
            print("Invalid input. Please, enter one of the available options.")
    return validated_task

def validate_numbers(message,error_message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)

