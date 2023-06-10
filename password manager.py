import bcrypt
from cryptography.fernet import Fernet

# Generate a master password
master_password = input("Enter a master password: ")
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(master_password.encode(), salt)

# Generate a strong password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(length))

# Encrypt and decrypt passwords
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    return decrypted_password.decode()

# Store passwords in a dictionary
passwords = {}
key = Fernet.generate_key()

# Add a new password
account_name = input("Enter the account name: ")
password = generate_password()
encrypted_password = encrypt_password(password, key)
passwords[account_name] = encrypted_password

# Retrieve a password
account_name = input("Enter the account name: ")
master_password = input("Enter the master password: ")
if bcrypt.checkpw(master_password.encode(), hashed_password):
    encrypted_password = passwords[account_name]
    password = decrypt_password(encrypted_password, key)
    print(f"The password for {account_name} is {password}")
else:
    print("Incorrect master password")