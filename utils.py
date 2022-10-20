"""

    Name: utils.py
    Author: Adam Frisch
    Created: 2/24/2022
    Purpose: A utility module with commonly used functions

"""

def get_int(prompt):
    """
        Get an integer from the user with try catch
        The prompt string parameter is used to ask the user
        for the type of input needed
    """
    # Declare local variable
    num = 0

    # Ask the user for an input based on the prompt string parameter
    num = input(prompt)

    #If the input is numeric, convert to int and return value
    try:
        return int(num)

    # If the input is not numeric,
    # Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a whole number.")
        print(f"Let's try that again.\n")

        # Call function from the beginning
        # This is a recursive function call
        return get_int(prompt)


def title(statement):
    """
        Takes in a string argument
        returns a string with ascii decorations
    """
    # Get the length of the statement
    text_length = len(statement)

    # Create the title string
    # Initialize the result string variable
    result = ""
    result = result + "+--" + "-" * text_length + "--+\n"
    result = result + "|  " + statement + "  |\n"
    result = result + "+--" + "-" * text_length + "--+\n"

    return result

def get_float(prompt):
    """
        Get a number from the user with try catch
        The prompt string parameter is used to ask the user
        for the type of input needed

    """

    # Declare local variable
    num = 0

    # Ask the user for an input based on the what parameter
    num = input(prompt)

    # If the input is numeric, convert to float and return value
    try:
        return float(num)

    # If the input is not numeric,
    # Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a number.")
        print(f"Let's try that again.\n")

        # Call function from the beginning
        # This is a recusive function call
        return get_float(prompt)

def main():
    """ Place code here to test the modules"""
    print(title("Test the utils module"))
    int_num = get_int("Please enter a whole number: ")
    print(f"Your whole number is: {int_num}")
    float_num = get_float("Please enter any number: ")
    print(f"Your number is: {float_num}")
    

# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
