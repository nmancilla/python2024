'''
- The password must be at least eight characters long.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one digit.
'''

import re

def validate_password(password):
    # define our regex pattern for validation
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"

    # We use the re.match function to test the password against the pattern
    match = re.match(pattern, password)

    # return True if the password matches the pattern, False otherwise
    return bool(match)

password1 = "StrongP@ssword123"
password2 = "weakpassword"
print(validate_password(password1)) 
print(validate_password(password2))  


# /*.[A+Z].*/