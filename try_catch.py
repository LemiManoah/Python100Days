def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(f"File content:\n{data}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found!")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'!")

def add_numbers(num1, num2):
    try:
        result = num1 + num2
        print(f"Result of addition: {result}")
    except TypeError:
        print("Error: Both inputs must be numbers!")

# Example Usage:
print("Division Example:")
divide_numbers(10, 0)  # Will trigger a ZeroDivisionError

print("\nFile Handling Example:")
read_file("non_existent_file.txt")  # Will trigger a FileNotFoundError

print("\nType Mismatch Example:")
add_numbers(10, "20")  # Will trigger a TypeError
