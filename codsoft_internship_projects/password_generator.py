import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):

    # Define the character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine all character sets
    all_chars = lower_chars + upper_chars + digits + special_chars

    # Ensure that we have at least one character to choose from
    if not all_chars:
        raise ValueError("No characters available for password generation")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        # Get user input
        length = int(input("Enter the desired length of the password: "))
        
        if length < 1:
            raise ValueError("Password length must be at least 1")

        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        # Generate and display the password
        password = generate_password(length, include_uppercase, include_digits, include_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
