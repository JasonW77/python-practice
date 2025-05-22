import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("No character sets selected!")
                
    return ''.join(random.choice(chars) for _ in range(length))
            
def main():
    print("🔐 Password Generator")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")
    except ValueError:
        print("❌ Please enter a valid positive number.")
        return
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"\n✅ Generated password: {password}")
    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()