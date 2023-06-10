import random
import string

def generate_password(length, uppercase, lowercase, numbers, special):
    # Create a list of characters based on user inputs
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special:
        chars += string.punctuation

    # Check if at least one character type is selected
    if not chars:
        return "Error: At least one character type must be selected."

    # Generate a random password of specified length
    password = ''.join(random.choice(chars) for i in range(length))

    # Check if the password meets complexity requirements
    if uppercase and not any(c.isupper() for c in password):
        return generate_password(length, uppercase, lowercase, numbers, special)
    if lowercase and not any(c.islower() for c in password):
        return generate_password(length, uppercase, lowercase, numbers, special)
    if numbers and not any(c.isdigit() for c in password):
        return generate_password(length, uppercase, lowercase, numbers, special)
    if special and not any(c in string.punctuation for c in password):
        return generate_password(length, uppercase, lowercase, numbers, special)

    return password

# Get user inputs
length = int(input("Enter the length of the password: "))
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
numbers = input("Include numbers? (y/n): ").lower() == 'y'
special = input("Include special characters? (y/n): ").lower() == 'y'
website = input("Enter the website name: ")

# Generate and print the password
password = generate_password(length, uppercase, lowercase, numbers, special)
print("Your password is:", password)

# Save the password and website name in a text file
with open('passwords.txt', 'a') as file:
    file.write(f"{website}: {password}\n")