import re
import getpass

PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%!?&*._-])[A-Za-z\d@$#%!?&*._-]{8,32}$")

def is_password_strong(password: str) -> bool:
    """
    Validate the strength of a password based on complexity requirements.
    Returns True if valid, False otherwise.
    """
    
    if not password:
        return False
    return bool(PASSWORD_REGEX.match(password))

def main():
    print("--- Password Strength Checker ---")
    
    password = getpass.getpass("Enter password to check: ")
    if is_password_strong(password):
        print("Password is strong.")
    else:
        print("Password is not strong!")
        print("Requirements: 8-32 chars, include Uppercase, Lowercase, Digit, and Special Char (@$#%!?&*._-).")
        
if __name__ == "__main__":
    main()