# Properly handled exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# Error depends on situation
i = int(input('Give me an integer: '))
# Error definately happens
print(10 / i)

# General
try:
    i = int(input('Give me an integer: '))
except:
    print("Error: Invalid input. Please enter an integer.")

# More accurate
try:
    i = int(input('Give me an integer: '))
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except:
    print("Error: Something went wrong.")   # This will catch all other exceptions that are not ValueError, like KeyboardInterrupt, EOFError, division by zero, printing errors, etc.

# Even more deep
try:
    i = int(input('Give me an integer: '))
except ValueError as value_error:
    print(f"Error: Invalid input {value_error}. Please enter an integer.")
except:
    print("Error: Something went wrong.")

# Ain't life wonderful?
try:
    x = int(input('Enter a number: '))
    result = 10 / x
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

# Finally we're getting somewhere
try:
    x = int(input('Enter a number: '))
    result = 10 / x
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")  # Code will only run if exception occurs
except ValueError:
    print("Error: Invalid input. Please enter a valid number.") # Code will only run if exception occurs
else:
    print("Result:", result)  # Code will only run if no exception occurs
finally:
    print("End of program.") # This block always runs, regardless of exceptions

# Custom error handling
class CustomError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise CustomError("Negative value not allowed.")

try:
    check_value(-5)
except CustomError as e:
    print("Error: ", e)


# Using built-in exceptions
class FileOperationError(IOError):
    pass

def read_file(file_name):
    try:
        with open(file_name, 'r') as file: # Using 'with' statement to ensure file is closed after reading
            contents = file.read()
    except FileNotFoundError:
        raise FileOperationError(f"File '{file_name}' not found.")
    
try:
    read_file('non_existent_file.txt')
except FileOperationError as e:
    print("Error: ", e)


