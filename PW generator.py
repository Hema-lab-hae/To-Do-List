import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character from each selected set is included
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length
    password += random.choices(char_pool, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

# Example usage:
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
