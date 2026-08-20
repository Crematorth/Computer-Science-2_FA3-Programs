# Asks the user to input a password and checks if it is between 8 and 20 characters long. If the password is invalid, it prompts the user to enter a new password until a valid one is provided.
password = input("Enter your password: ")

# Loop to check the length of the password
while len(password) < 8 or len(password) > 20:
    # If the password is invalid, print an error message and prompt the user to enter a new password
    print("Password is invalid. It must be between 8 and 20 characters long.")
    password = input("Enter your password: ")

# If the password is valid, print a success message
print("Password is valid.")