import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short!"
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    if length >= 12 and has_upper and has_digit and has_symbol:
        return "Strong"
    elif length >= 8:
        return "Medium"
    else:
        return "Weak"
    
while True:
    print("\n Welcome users")
    print("1. Generate a strong password")
    print("2. Check the strength of your password")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        length = int(input("Enter desired password length: "))
        password = generate_password(length)

        if "too short" in password:
            print(password)
        else:
            print(f"\nGenerated Password: {password}")
            print(f"Password Strength: {check_strength(password)}")

    elif choice == "2":
        user_password = input("Enter your password: ")
        print(f"Password Strength: {check_strength(user_password)}")

    elif choice == "3":
        print("Goodbye!")
        break 

    else:
        print("Invalid option. Please enter 1, 2, or 3.")
