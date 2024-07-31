import re
from datetime import datetime
    
def validate_email(email,allowed_domains,pattern):
    try:
        if email.count('@') != 1:
            raise ValueError("Invalid email format. The email must contain Domain part.")

        domain_part = email.split('@')
        domain = domain_part[1].split('.')[0]
        
        if domain not in allowed_domains:
            raise ValueError("Sorry for the inconvenience, we only allow domains like gmail and yahoo.")

        if not re.match(pattern, email):
           raise ValueError("Invalid email format or domain.")
        else:
            return True
            
    except ValueError as ve:
       raise ve
    except Exception as e:
        raise e


def validate_dob(dob: str):
    try:
        # Attempt to parse the date with the expected format
        datetime.strptime(dob, '%d/%m/%Y')
        return True
    except ValueError:
        # Raise a ValueError if the date format is invalid
        raise ValueError(f"The provided date '{dob}' is invalid. Please use the format dd/mm/yyyy.")
    
def validate_password(password: str):
    try:
        # Password must be at least 8 characters long
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        # Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character
        if not re.search(r'[A-Z]', password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password):
            raise ValueError("Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError("Password must contain at least one special character.")
        return password
    except ValueError as ve:
       raise ve
    except Exception as e:
        raise e
    
def confirm_password(confirm_password: str,password: str):
    try:
            # Check if the confirmed password matches the original password
        if password != confirm_password:
            raise ValueError("Password and confirm_password do not match.")
    except ValueError as ve:
        raise ve

