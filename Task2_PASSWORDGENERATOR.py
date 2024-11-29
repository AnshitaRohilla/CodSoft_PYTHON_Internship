# PASSWORD GENERATOR
import random
import string

# Function to generate a random password
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generates a random password with the specified parameters.
    
    Parameters:
    - length (int): Length of the generated password.
    - use_upper (bool): Whether to include uppercase letters.
    - use_lower (bool): Whether to include lowercase letters.
    - use_digits (bool): Whether to include digits.
    - use_special (bool): Whether to include special characters.
    
    Returns:
    - password (str): The generated password.
    """
    # Create an empty list to hold the character sets to include in the password
    character_sets = []
    
    if use_upper:
        character_sets.append(string.ascii_uppercase)  # A-Z
    if use_lower:
        character_sets.append(string.ascii_lowercase)  # a-z
    if use_digits:
        character_sets.append(string.digits)  # 0-9
    if use_special:
        character_sets.append(string.punctuation)  # Special characters like !@#$%^&*

    # If no character sets are selected, raise an error
    if not character_sets:
        raise ValueError("At least one character set (uppercase, lowercase, digits, special) must be selected.")
    
    # Combine all selected character sets into one string
    all_characters = ''.join(character_sets)
    
    # Generate a random password by selecting random characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Main program
if __name__== "__main__":
    print("Welcome to the Random Password Generator!")
    
    try:
        # User input for password length
        length = int(input("Enter the desired password length: "))
        
        # User input for including different character sets
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate the password
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        
        # Display the generated password
        print(f"Your generated password is: {password}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")