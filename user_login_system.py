"""
Paso 1: Construir la logica del Log In.
Crear un archivo JSON donde guardemos los datos de los clientes (nombre,dni,email,cuenta bancaria) y que cuenta bancaria sea un diccionario

Primer paso: Agregar esta info al JSON.
"""
import json

customer_data_file = "data/tasks.json"
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

def introduction():
    print("Hello user, this is a bank account simulator")
    print("Please choose an option of the following: ")
    print("1- Register")
    print("2- Log in")


