import random
import string

def generate_strong_password(length):
    if length < 4:
        return "Password length must be at least 4"
    
    # Ensure at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),  # lowercase
        random.choice(string.ascii_uppercase),  # uppercase
        random.choice(string.digits),           # digit
        random.choice(string.punctuation)       # symbol
    ]
    
    # Fill the remaining length with random characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(characters) for _ in range(length - 4)]
    
    # Shuffle to mix the characters
    random.shuffle(password)
    
    return "".join(password)

print("=== STRONG PASSWORD GENERATOR ===")

while True:
    length = int(input("Enter password length (enter 0 to exit): "))
    if length == 0:
        print("Exiting program...")
        break
    password = generate_strong_password(length)
    print("Generated strong password:", password)