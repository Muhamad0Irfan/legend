import re

username_pattern = r'^[a-zA-Z]+$'
password_pattern = r'^(?=.*\d)(?=.*[@$!%*#?&])(?=.*[A-Z]).{7,}$'

# Prompt the user for a username and password
username = input("Enter your username (alphabetical only): ")
password = input("Enter your password (at least 7 characters with a digit, special character, and uppercase letter): ")

if not re.match(username_pattern, username):
    print("Invalid username! Username must be all alphabetical.")
elif not re.match(password_pattern, password):
    print("Invalid password! Password must be at least 7 characters with a digit, special character, and uppercase letter.")
else:
    print("You are logged into the system")